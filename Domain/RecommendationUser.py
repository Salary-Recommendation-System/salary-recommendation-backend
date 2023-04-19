from Domain.MainUser import MainUser


class RecommendationUser(MainUser):

    def __init__(self, education_level, work_experience, designation, created_date_time,
                 user_rating, no_of_employees, recommendation):
        super().__init__(education_level, work_experience, designation, created_date_time, user_rating, no_of_employees)
        self.__recommendation = recommendation

    def get_recommendation(self):
        return self.__recommendation

    def set_recommendation(self, recommendation):
        self.__recommendation = recommendation
