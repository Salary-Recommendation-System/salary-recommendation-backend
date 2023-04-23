import psycopg2.errors

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import  open_connection
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
            with open_connection().cursor() as cursor:
                if amount is None:
                    query = UserInformationQueryUtils.get_all_information(work_experience, education, designation,
                                                                          no_of_employees)

                    cursor.execute(query)
                    information = cursor.fetchall()
                    dataframe = pd.DataFrame(information,
                                             columns=["id", "education_level", "work_experience", "designation",
                                                      "created_date_time","salary_amount", "no_of_employees",
                                                      "primary_technology", "user_rating", "year_of_payment"])
                    return dataframe
                else:
                    query = UserInformationQueryUtils.get_information(work_experience, education, designation,
                                                                      no_of_employees,
                                                                      amount)
                    cursor.execute(query)
                    information = cursor.fetchall()
                    dataframe = pd.DataFrame(information,
                                             columns=["id", "education_level", "work_experience", "designation",
                                                      "created_date_time","salary_amount", "no_of_employees",
                                                      "primary_technology", "user_rating", "year_of_payment"])
                    return dataframe
        except psycopg2.errors.ConnectionException:
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
        except Exception as e:
            print(e)
            return Response(e, 400)
