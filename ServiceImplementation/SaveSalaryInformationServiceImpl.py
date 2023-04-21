from Domain.VO.RatingParameterVo import RatingParameterVo
from Repository.writer.SaveInformationUserWriterRepository import SaveInformationUserWriterRepository
from Service.SaveSalaryInformationService import SaveSalaryInformationService
import logging
from Utils.Message import Message
from Utils.Response import Response
import pandas as pd


def convert_to_lkr(currency_type, salary_amount):
    if currency_type == 'USD':
        return salary_amount * 325
    elif currency_type == 'GBP':
        return salary_amount * 402
    elif currency_type == 'JPY':
        return salary_amount * 2
    elif currency_type == 'AUD':
        return salary_amount * 217
    elif currency_type == 'SGD':
        return salary_amount * 243
    elif currency_type == 'NZD':
        return salary_amount * 200
    elif currency_type == 'EUR':
        return salary_amount * 355
    elif currency_type == 'CAD':
        return salary_amount * 242
    elif currency_type == 'CHF':
        return salary_amount * 361
    else:
        return salary_amount


class SaveSalaryInformationServiceImpl(SaveSalaryInformationService):
    logging.basicConfig(filename='SaveSalaryInformationServiceImpl.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')

    def save(self,db_session, information_user):

        logging.info("SaveSalaryInformationServiceImpl: save salary information")
        if information_user.get_salary_amount() is None:
            logging.info("SaveSalaryInformationServiceImpl: Salary information is incorrect")
            return Response(Message.SALARY.value, Message.SALARY.message)
        elif information_user.get_no_of_employees() is None:
            logging.info("SaveSalaryInformationServiceImpl: Number of employees is None")
            return Response(Message.NO_OF_EMPLOYEES.value, Message.NO_OF_EMPLOYEES.message)
        else:
            information_user.set_salary_amount(convert_to_lkr(information_user.get_currency_type(),
                                                              float(information_user.get_salary_amount())))

            saving_information = SaveInformationUserWriterRepository()
            saving_information.save(db_session,information_user)
            logging.info("SaveSalaryInformationServiceImpl: Successfully saved the information's provided")
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)

    def save_existing_data(self,db_session):
        try:

            save_information = SaveInformationUserWriterRepository()
            data = pd.read_csv("Utils/Files/unique_salary.csv")
            return save_information.save_from_excel(db_session,data)

        except Exception as e:
            print(e)
            return Response(Message.UNIQUE_SALARY_FILE_NOT_FOUND.value, Message.UNIQUE_SALARY_FILE_NOT_FOUND.message)

    def update_rating(self,db_session, rating, id):
        save_information = SaveInformationUserWriterRepository()
        return save_information.update_rating(db_session,rating, id)
