import psycopg2.errors

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import db_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import UserInformationQueryUtils
import pandas as pd
import psycopg2
from Resources.Config import Config


class SaveInformationUserReaderRepository(SaveInformationUserRepository):

    def get_all_saved_information(self, work_experience, education, designation, no_of_employees,amount):
        try:
            config = Config()
            connection = psycopg2.connect(database=config.get('name'), user=config.get('user'),
                                          password=config.get('password'),
                                          host=config.get('host'))
            if amount is None:
                query = UserInformationQueryUtils.get_all_information(work_experience, education, designation,
                                                                      no_of_employees)
                print(query)
                dataframe = pd.read_sql(query, connection)
                connection.close()
                return dataframe
            else:
                query = UserInformationQueryUtils.get_information(work_experience,education,designation,no_of_employees,
                                                                  amount)
                dataframe = pd.read_sql(query, connection)
                connection.close()
                return dataframe
        except psycopg2.errors.ConnectionException:
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
        except Exception as e:
            print(e)
            return Response(e, 400)

    def save(self, information_user):
        pass

    def create(self, schema_name):
        pass

    def save_from_excel(self, information):
        pass

    def update_rating(self,rating, id):
        pass
