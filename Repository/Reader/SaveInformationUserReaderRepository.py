from sqlalchemy.exc import SQLAlchemyError

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import SalaryDetail
from Utils.Response import Response
import pandas as pd


class SaveInformationUserReaderRepository(SaveInformationUserRepository):

    def get_all_saved_information(self, db_session, work_experience, education, designation, no_of_employees, amount):
        try:
            if amount is None:
                try:
                    filters = [
                        SalaryDetail.work_experience == str(work_experience),
                        SalaryDetail.education_level == str(education),
                        SalaryDetail.designation == str(designation),
                        SalaryDetail.no_of_employees == str(no_of_employees)

                    ]
                    result = db_session.query(SalaryDetail).filter(*filters).all()

                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame([(r.id,r.education_level, r.work_experience, r.designation, r.salary_amount,
                                               r.created_date_time, r.no_of_employees, r.primary_technology,
                                               r.user_rating, r.year_of_payment) for r in result],
                                             columns=["id","education_level", "work_experience", "designation",
                                                      "salary_amount", "created_date_time", "no_of_employees",
                                                      "primary_technology", "user_rating", "year_of_payment"])

                    # Return the DataFrame
                    return dataframe
                except Exception as e:
                    result = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation)).all()
                    dataframe = pd.DataFrame([r.__dict__ for r in result])
                    dataframe = dataframe.drop('_sa_instance_state', axis=1)
                    return dataframe

            else:
                try:

                    filters = [
                        SalaryDetail.work_experience == str(work_experience),
                        SalaryDetail.education_level == str(education),
                        SalaryDetail.designation == str(designation),
                        SalaryDetail.no_of_employees == str(no_of_employees),
                        SalaryDetail.salary_amount == float(amount)
                    ]

                    result = db_session.query(SalaryDetail).filter(*filters).all()

                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame([row.__dict__ for row in result])

                    # Remove the ORM objects from the DataFrame
                    dataframe = dataframe.drop('_sa_instance_state', axis=1)
                    return dataframe
                except Exception as e:
                    result = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation)).all()
                    dataframe = pd.DataFrame([r.__dict__ for r in result])
                    dataframe = dataframe.drop('_sa_instance_state', axis=1)
                    return dataframe

        except SQLAlchemyError as e:
            db_session.rollback()
        except Exception as e:
            print(e)
            return Response(e, 400)

    def save(self, db_session, information_user):
        pass

    def create(self, db_session, schema_name):
        pass

    def save_from_excel(self, db_session, information):
        pass

    def update_rating(self, db_session, rating, id):
        pass
