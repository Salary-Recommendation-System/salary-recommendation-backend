from datetime import datetime

from Repository.EncodedSalaryRepository import EncodedSalaryRepository
from Resources.Database import EncodedSalaryConversion, EncodedSalary
from Utils.Message import Message
from Utils.Response import Response


class EncodedSalaryWriterRepository(EncodedSalaryRepository):

    def save(self, db_session, encode_information):
        try:

            for index, row in encode_information.iterrows():
                encoded_salary = EncodedSalary(education_level=int(row['Education']),
                                               work_experience=int(row['Work experience']),
                                               designation=int(row['Designation']), salary_amount=float(row['Amount']),
                                               created_date_time=datetime.now(),
                                               no_of_employees=int(row['Company size']))
                db_session.add(encoded_salary)
            db_session.commit()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def save_encode_data(self, db_session, binary_information):
        try:
            for index, row in binary_information.iterrows():
                encoded_salary_conversion = EncodedSalaryConversion(encoded_value=row['Encode value'],
                                                                    unique_code=row['code'])
                db_session.add(encoded_salary_conversion)
            db_session.commit()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def get_encode_data(self, db_session, work_experience, education, company_size, designation):
        pass
