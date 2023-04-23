import psycopg2.errors

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import SalaryDetail, db_connection
from Utils.Message import Message
from Utils.Response import Response
import pandas as pd

from Utils.Scripts import UserInformationQueryUtils


class SaveInformationUserReaderRepository(SaveInformationUserRepository):

    def save(self, information_user):
        pass

    def save_from_excel(self, information):
        pass

    def update_rating(self, rating, id):
        pass

    def create(self, schema_name):
        pass

    def get_all_saved_information(self, work_experience, education, designation, no_of_employees, amount):
        try:
            database = db_connection()

            if amount is None:
                query = UserInformationQueryUtils.get_all_information(work_experience, education, designation,
                                                                      no_of_employees)

                database.cursor.execute(query)
                information = database.cursor.fetchall()

                dataframe = pd.DataFrame([(r.id, r.education_level, r.work_experience, r.designation, r.salary_amount,
                                           r.created_date_time, r.no_of_employees, r.primary_technology,
                                           r.user_rating, r.year_of_payment) for r in information],
                                         columns=["id", "education_level", "work_experience", "designation",
                                                  "salary_amount", "created_date_time", "no_of_employees",
                                                  "primary_technology", "user_rating", "year_of_payment"])

                database.cursor.close()
                database.connection.close()
                return dataframe
            else:
                query = UserInformationQueryUtils.get_information(work_experience, education, designation,
                                                                  no_of_employees,
                                                                  amount)
                database.cursor.execute(query)
                information = database.cursor.fetchall()
                dataframe = pd.DataFrame([(r.id, r.education_level, r.work_experience, r.designation, r.salary_amount,
                                           r.created_date_time, r.no_of_employees, r.primary_technology,
                                           r.user_rating, r.year_of_payment) for r in information],
                                         columns=["id", "education_level", "work_experience", "designation",
                                                  "salary_amount", "created_date_time", "no_of_employees",
                                                  "primary_technology", "user_rating", "year_of_payment"])
                database.cursor.close()
                database.connection.close()
                return dataframe
        except psycopg2.errors.ConnectionException:
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
        except Exception as e:
            print(e)
            return Response(e, 400)
