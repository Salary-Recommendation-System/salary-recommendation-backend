from datetime import datetime

import psycopg2.errors

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import SalaryDetail, db_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import UserInformationQueryUtils


class SaveInformationUserWriterRepository(SaveInformationUserRepository):

    def save(self, information_user):

        try:
            database = db_connection()
            save_query = UserInformationQueryUtils.save(information_user.get_education_level(),
                                                        information_user.get_work_experience(),
                                                        information_user.get_designation(),
                                                        information_user.get_created_date_time(),
                                                        information_user.get_salary_amount(),
                                                        information_user.get_no_of_employees(),
                                                        information_user.get_primary_technology(),
                                                        information_user.get_user_rating(),
                                                        information_user.get_year_of_payment())

            print(save_query)
            database.cursor.execute(save_query)
            database.connection.commit()
            database.cursor.close()
            database.connection.close()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def save_from_excel(self, information):

        try:
            database = db_connection()

            for index, row in information.iterrows():
                save_query = UserInformationQueryUtils.save(row['Education'], row['Work experience'],
                                                            row['Designation'], datetime.now(), int(row['Amount']),
                                                            row['Company size'], '', 2.0, int(row['Year']))
                database.cursor.execute(save_query)

            database.connection.commit()
            database.cursor.close()
            database.connection.close()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)

        except psycopg2.errors.SavepointException:
            return Response(Message.SAVING_FAILED.value, Message.SAVING_FAILED.message)

        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def update_rating(self, rating,id):
        try:
            database = db_connection()
            update_query = UserInformationQueryUtils.update_rating(rating,id)
            database.cursor.execute(update_query)
            database.connection.commit()
            database.cursor.close()
            database.connection.close()
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
            database = db_connection()
            create_query = UserInformationQueryUtils.create(schema_name)
            database.cursor.execute(create_query)
            database.connection.commit()
            database.cursor.close()
            database.connection.close()
            return Response(Message.DB_TABLE_CREATED.value, Message.DB_TABLE_CREATED.message)
        except psycopg2.errors.DuplicateTable:
            return Response(Message.DB_TABLE_ALREADY_CREATED.value, Message.DB_TABLE_ALREADY_CREATED.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

