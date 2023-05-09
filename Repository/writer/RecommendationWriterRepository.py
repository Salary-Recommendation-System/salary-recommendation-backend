import uuid
from datetime import datetime

from Repository.RecommendationRepository import RecommendationRepository
from Resources.Database import RecommendationDetail, create_database_engine
from Utils.Message import Message
from Utils.Response import Response


class RecommendationWriterRepository(RecommendationRepository):

    def save(self, db_session, recommendation_user):
        uniqueid = uuid.uuid1()
        engine = create_database_engine()
        try:
            with engine.connect() as connection:

                for key, values in recommendation_user.get_recommendation().items():
                    for item in values:
                        recommendation_details = RecommendationDetail(education_level=item['education_level'],
                                                                      work_experience=item['work_experience'],
                                                                      designation=item['designation'],
                                                                      created_date_time=datetime.now(),
                                                                      user_rating=item['user_rating'],
                                                                      no_of_employees=item['no_of_employees'],
                                                                      salary_amount=item['salary_amount'],
                                                                      batch_id=uniqueid,
                                                                      inflation_rate=item['inflation_rate'],
                                                                      inflation_amount=item['inflation_amount'])
                        connection.execute(recommendation_details.__table__.insert(), recommendation_details.__dict__)
                connection.commit()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
