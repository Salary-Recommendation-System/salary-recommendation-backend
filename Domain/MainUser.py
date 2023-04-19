class MainUser:

    def __init__(self, education_level, work_experience, designation, created_date_time, user_rating, no_of_employees):
        self.__education_level = education_level
        self.__work_experience = work_experience
        self.__designation = designation
        self.__created_date_time = created_date_time
        self.__user_rating = user_rating
        self.__no_of_employees = no_of_employees

    def get_education_level(self):
        return self.__education_level

    def set_education_level(self, education_level):
        self.__education_level = education_level

    def get_work_experience(self):
        return self.__work_experience

    def set_work_experience(self, work_experience):
        self.__work_experience = work_experience

    def get_designation(self):
        return self.__designation

    def set_designation(self, designation):
        self.__designation = designation

    def get_created_date_time(self):
        return self.__created_date_time

    def set_created_date_time(self, created_date_time):
        self.__created_date_time = created_date_time

    def get_user_rating(self):
        return self.__user_rating

    def set_user_rating(self, user_rating):
        self.__user_rating = user_rating

    def get_no_of_employees(self):
        return self.__no_of_employees

    def set_no_of_employees(self, no_of_employees):
        self.__no_of_employees = no_of_employees

    def __str__(self):
        return f"MainUser(education_level='{self.__education_level}', work_experience='{self.__work_experience}', designation='{self.__designation}', created_date_time='{self.__created_date_time}')"
