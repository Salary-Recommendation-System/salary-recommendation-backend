from datetime import datetime

import psycopg2.errors

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import open_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import UserInformationQueryUtils


class SaveInformationUserWriterRepository(SaveInformationUserRepository):

    def get_all_saved_information(self, work_experience, education, designation, no_of_employees, amount):
        pass

    def save(self, information_user):

        try:
            with open_connection().cursor() as cursor:
                save_query = UserInformationQueryUtils.save(information_user.get_education_level(),
                                                            information_user.get_work_experience(),
                                                            information_user.get_designation(),
                                                            information_user.get_created_date_time(),
                                                            information_user.get_salary_amount(),
                                                            information_user.get_no_of_employees(),
                                                            information_user.get_primary_technology(),
                                                            information_user.get_user_rating(),
                                                            information_user.get_year_of_payment())

                cursor.execute(save_query)
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def save_from_excel(self, information):

        try:
            with open_connection().cursor() as cursor:

                for index, row in information.iterrows():
                    save_query = UserInformationQueryUtils.save(row['Education'], row['Work experience'],
                                                                row['Designation'], datetime.now(), int(row['Amount']),
                                                                row['Company size'], '', 2.0, int(row['Year']))
                    cursor.execute(save_query)
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)

        except psycopg2.errors.SavepointException:
            return Response(Message.SAVING_FAILED.value, Message.SAVING_FAILED.message)

        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def update_rating(self, rating, id):
        try:
            with open_connection().cursor() as cursor:
                update_query = UserInformationQueryUtils.update_rating(rating, id)
                cursor.execute(update_query)
            return Response(Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.value,
                            Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.message)
        except psycopg2.errors.DataException:
            return Response(Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.value,
                            Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.message)
        except Exception as e:
            print(e)
            return Response(Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.value,
                            Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.message)

    def create(self, schema_name):
        try:
            with open_connection().cursor() as cursor:
                create_query = UserInformationQueryUtils.create(schema_name)
                cursor.execute(create_query)
            return Response(Message.DB_TABLE_CREATED.value, Message.DB_TABLE_CREATED.message)
        except psycopg2.errors.DuplicateTable:
            return Response(Message.DB_TABLE_ALREADY_CREATED.value, Message.DB_TABLE_ALREADY_CREATED.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
