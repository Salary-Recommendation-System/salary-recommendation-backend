from Domain.MainUser import MainUser


class RecommendationUser(MainUser):

    def __init__(self, education_level, work_experience, designation, created_date_time,
                 user_rating, no_of_employees, recommendation, inflation_rate):
        super().__init__(education_level, work_experience, designation, created_date_time, user_rating, no_of_employees)
        self.__recommendation = recommendation
        self.__inflation_rate = inflation_rate

    def get_recommendation(self):
        return self.__recommendation

    def set_recommendation(self, recommendation):
        self.__recommendation = recommendation

    def get_inflation_rate(self):
        return self.__inflation_rate

    def set_inflation_rate(self, inflation_rate):
        self.__inflation_rate = inflation_rate
