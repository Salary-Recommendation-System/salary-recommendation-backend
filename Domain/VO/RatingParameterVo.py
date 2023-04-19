from Domain.InformationUser import InformationUser


class RatingParameterVo(InformationUser):

    def __init__(self, education_level, work_experience, designation, created_date_time, salary_amount, no_of_employees,
                 primary_technology, user_rating, year_of_payment, last_updated_time):
        super().__init__(education_level, work_experience, designation, created_date_time, salary_amount,
                         no_of_employees, primary_technology, user_rating, year_of_payment)
        self.__last_updated_time = last_updated_time

    def get_last_updated_time(self):
        return self.get_created_date_time()

    def set_last_updated_time(self, last_updated_time):
        self.__last_updated_time = last_updated_time



