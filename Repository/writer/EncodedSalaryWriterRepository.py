from datetime import datetime

import psycopg2.errors

from Domain.InformationUser import InformationUser
from Repository.EncodedSalaryRepository import EncodedSalaryRepository
from Resources.Database import db_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import EncodedSalaryDetailUtils


class EncodedSalaryWriterRepository(EncodedSalaryRepository):

    def save(self, encode_information):
        try:
            database = db_connection()

            for index, row in encode_information.iterrows():
                information = InformationUser(row['Education'], row['Work experience'], row['Designation'],
                                              datetime.now(),
                                              row['Amount'], row['Company size'], '', '', '','')
                save_query = EncodedSalaryDetailUtils.save(information)
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

    def create(self, schema_name, encoded_table):
        try:
            database = db_connection()

            if bool(encoded_table):
                create_query = EncodedSalaryDetailUtils.create_encode_table_with_user_inputs(schema_name)
                database.cursor.execute(create_query)
            else:
                create_query = EncodedSalaryDetailUtils.create(schema_name)
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

    def save_encode_data(self, binary_information):
        try:
            database = db_connection()
            for index, row in binary_information.iterrows():

                save_query = EncodedSalaryDetailUtils.save_encode_data(row['Encode value'], row['code'])
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