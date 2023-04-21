from sqlalchemy.exc import SQLAlchemyError

from Repository.EncodedSalaryRepository import EncodedSalaryRepository
from Resources.Database import db_connection, EncodedSalaryConversion
from Utils.Message import Message
from Utils.Response import Response
import psycopg2.errors


class EncodedSalaryReaderRepository(EncodedSalaryRepository):

    def get_encode_data(self, db_session, work_experience, education, company_size, designation):
        try:
            data = db_session.query(EncodedSalaryConversion).filter(
                EncodedSalaryConversion.unique_code.in_(
                    [str(work_experience), str(education), str(company_size), str(designation)]
                )
            ).all()

            return data
        except SQLAlchemyError as e:
            db_session.rollback()
        except Exception as e:
            print(e)
            return Response(e, 400)

    def save(self, db_session, encode_information):
        pass

    def save_encode_data(self, db_session, binary_information):
        pass
