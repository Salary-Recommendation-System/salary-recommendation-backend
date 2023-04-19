from Repository.EncodedSalaryRepository import EncodedSalaryRepository
from Resources.Database import db_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import EncodedSalaryDetailUtils
import psycopg2.errors


class EncodedSalaryReaderRepository(EncodedSalaryRepository):

    def get_encode_data(self, work_experience, education, company_size, designation):
        try:
            database = db_connection()
            query = EncodedSalaryDetailUtils.get_based_on_parameters(work_experience, education, company_size,
                                                                     designation)
            database.cursor.execute(query)
            information = database.cursor.fetchall()
            database.cursor.close()
            database.connection.close()
            return information
        except psycopg2.errors.ConnectionException:
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
        except Exception as e:
            print(e)
            return Response(e, 400)

    def create(self, schema_name, encoded_table):
        pass

    def save(self, encode_information):
        pass

    def save_encode_data(self, binary_information):
        pass
