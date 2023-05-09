import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from Repository.Reader.SaveInformationUserReaderRepository import SaveInformationUserReaderRepository
from Repository.writer.RecommendationWriterRepository import RecommendationWriterRepository
from Service.GetRecommendationService import GetRecommendationService
from ServiceImplementation.EncodedSalaryServiceImpl import EncodedSalaryServiceImpl
from ServiceImplementation.InflationServiceImpl import InflationServiceImpl
from Utils.Message import Message
from Utils.Response import Response
import threading
import pandas as pd


def save_in_different_thread(db_session, recommendation_user):
    recommendation_writer_repository = RecommendationWriterRepository()
    return recommendation_writer_repository.save(db_session, recommendation_user)


def add_inflation_details(salaries, db_session):
    inflation = InflationServiceImpl()
    rates = inflation.get_inflation(db_session)
    if len(rates) != 0:
        for salary in salaries:
            rate = rates[0]
            inflation_amount = float(salary['salary_amount']) * float(rate)
            salary['inflation_rate'] = format((1 - rate) * 100, ".2f")
            salary['inflation_amount'] = round(float(inflation_amount))
        return salaries
    return salaries


def content_based_filtering(db_session, saved_information, work_experience, education, designation, no_of_employees,
                            amount, n=10):
    try:
        data = saved_information.get_all_saved_information(db_session, work_experience, education, designation,
                                                           no_of_employees, None)

        if len(data) != 0:
            data = data.drop(['created_date_time'], axis=1)
            data['text_features'] = data['work_experience'] + ' ' + data['education_level'] + ' ' + data[
                'no_of_employees'] + ' ' + data['designation']
            vectorized = TfidfVectorizer()
            tfidf_matrix = vectorized.fit_transform(data['text_features'])
            input_vec = tfidf_matrix[data.index[0]]
            sim_scores = cosine_similarity(input_vec, tfidf_matrix)[0]
            sim_indices = sim_scores.argsort()[::-1][1:n + 1]

            similar_data = data.iloc[sim_indices][['id', 'work_experience', 'education_level', 'no_of_employees',
                                                   'designation', 'salary_amount', 'user_rating', 'year_of_payment',
                                                   'primary_technology']]
            if amount is not None:
                similar_data = similar_data[similar_data['salary_amount'] != int(amount)]
                return similar_data
            else:
                return similar_data
        else:
            return []
    except Exception as e:
        print(e)


class GetRecommendationServiceImpl(GetRecommendationService):

    def save(self, db_session, recommendation_user):

        recommendation = {}
        try:

            with open('Utils/Files/salary_recommendation.pkl', 'rb') as file:
                saved_model = pickle.load(file)
        except Exception as e:
            print(e)

        # Reading from the Database the relevant encoded values
        encoded_service_impl = EncodedSalaryServiceImpl()
        encoded_service_impl = encoded_service_impl.get_encode_data(db_session,
                                                                    recommendation_user.get_work_experience(),
                                                                    recommendation_user.get_education_level(),
                                                                    recommendation_user.get_no_of_employees(),
                                                                    recommendation_user.get_designation())
        saved_information = SaveInformationUserReaderRepository()
        if len(encoded_service_impl) != 0:
            try:
                user_inputs = pd.DataFrame({
                    'Work experience': [encoded_service_impl[0].encoded_value],
                    'Education': [encoded_service_impl[1].encoded_value],
                    'Company size': [encoded_service_impl[2].encoded_value],
                    'Designation': [encoded_service_impl[3].encoded_value]
                })
                prediction = saved_model.predict(user_inputs)
                if len(prediction) != 0:
                    dataframe = content_based_filtering(db_session, saved_information,
                                                        recommendation_user.get_work_experience(),
                                                        recommendation_user.get_education_level(),
                                                        recommendation_user.get_designation(),
                                                        recommendation_user.get_no_of_employees(),
                                                        prediction[0], 5)

                    predicted_information = saved_information.get_all_saved_information(
                        db_session,
                        recommendation_user.get_work_experience(),
                        recommendation_user.get_education_level(),
                        recommendation_user.get_designation(),
                        recommendation_user.get_no_of_employees(),
                        prediction[0])

                    if len(dataframe) == 0:
                        recommendation['content_based_filtering'] = []
                        recommendation['label_message'] = Message.BEST_MATCH_NO_FOUND
                    else:
                        recommendation['content_based_filtering'] = dataframe.to_dict(orient='records')

                    if len(predicted_information) > 0:
                        recommendation['model_filtering'] = predicted_information.to_dict(orient='records')
                    else:
                        recommendation['model_filtering'] = []
                        recommendation['label_message'] = ""

                else:
                    dataframe = content_based_filtering(db_session, saved_information,
                                                        recommendation_user.get_work_experience(),
                                                        recommendation_user.get_education_level(),
                                                        recommendation_user.get_designation(),
                                                        recommendation_user.get_no_of_employees(), None, 5)
                    if len(dataframe) == 0:
                        recommendation['content_based_filtering'] = []
                        recommendation['label_message'] = Message.BEST_MATCH_NO_FOUND
                    else:
                        recommendation['content_based_filtering'] = dataframe.to_dict(orient='records')

                    recommendation['model_filtering'] = []
            except Exception as e:
                print(e)
                print("Model access failure, due to lack of information", e)
                dataframe = content_based_filtering(db_session, saved_information,
                                                    recommendation_user.get_work_experience(),
                                                    recommendation_user.get_education_level(),
                                                    recommendation_user.get_designation(),
                                                    recommendation_user.get_no_of_employees(), None, 5)
                if len(dataframe) == 0:
                    recommendation['content_based_filtering'] = []
                    recommendation['label_message'] = Message.BEST_MATCH_NO_FOUND
                else:
                    recommendation['content_based_filtering'] = dataframe.to_dict(orient='records')
                recommendation['model_filtering'] = []
        else:
            dataframe = content_based_filtering(db_session, saved_information,
                                                recommendation_user.get_work_experience(),
                                                recommendation_user.get_education_level(),
                                                recommendation_user.get_designation(),
                                                recommendation_user.get_no_of_employees(), None, 5)
            if len(dataframe) == 0:
                recommendation['content_based_filtering'] = []
                recommendation['label_message'] = Message.BEST_MATCH_NO_FOUND
            else:
                recommendation['content_based_filtering'] = dataframe.to_dict(orient='records')
            recommendation['model_filtering'] = []

        content_salary = add_inflation_details(recommendation['content_based_filtering'],db_session)
        model_salary = add_inflation_details(recommendation['model_filtering'],db_session)

        updated_recommendation = {'content_based_filtering': content_salary, 'model_filtering': model_salary}

        recommendation_user.set_recommendation(updated_recommendation)
        print(updated_recommendation)
        # recommendation_user.set_inflation_rate(inflation_service.get_inflation(db_session))
        thread = threading.Thread(target=save_in_different_thread, args=(db_session, recommendation_user,))
        thread.start()

        return Response(Message.SUCCESS_MESSAGE.value, updated_recommendation)
