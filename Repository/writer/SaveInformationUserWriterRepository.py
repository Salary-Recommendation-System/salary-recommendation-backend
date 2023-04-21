from datetime import datetime

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import SalaryDetail
from Utils.Message import Message
from Utils.Response import Response


class SaveInformationUserWriterRepository(SaveInformationUserRepository):

    def save(self, db_session, information_user):

        try:
            salary_details = SalaryDetail(education_level=information_user.get_education_level(),
                                          work_experience=information_user.get_work_experience(),
                                          designation=information_user.get_designation(),
                                          created_date_time=information_user.get_created_date_time(),
                                          salary_amount=information_user.get_salary_amount(),
                                          no_of_employees=information_user.get_no_of_employees(),
                                          primary_technology=information_user.get_primary_technology(),
                                          user_rating=information_user.get_user_rating(),
                                          year_of_payment=information_user.get_year_of_payment())
            db_session.add(salary_details)
            db_session.commit()

            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def save_from_excel(self, db_session, information):
        try:
            for index, row in information.iterrows():
                salary_details = SalaryDetail(education_level=row['Education'], work_experience=row['Work experience'],
                                              designation=row['Designation'], created_date_time=datetime.now(),
                                              salary_amount=int(row['Amount']), no_of_employees=row['Company size'],
                                              primary_technology='', user_rating=2.0, year_of_payment=int(row['Year']))
                db_session.add(salary_details)
            db_session.commit()
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def update_rating(self, db_session, rating, id):
        try:

            db_session.query(SalaryDetail).filter(SalaryDetail.id == id).update({'user_rating': rating})
            db_session.commit()
            return Response(Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.value,
                            Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.message)
        except Exception as e:
            print(e)
            return Response(Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.value,
                            Message.SUCCESSFULLY_UPDATED_WITH_INFORMATION.message)

    def get_all_saved_information(self, db_session, work_experience, education, designation, no_of_employees, amount):
        pass
