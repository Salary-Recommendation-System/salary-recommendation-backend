from Domain.MainUser import MainUser


class InformationUser(MainUser):

    def __init__(self, education_level, work_experience, designation, created_date_time, salary_amount, no_of_employees,
                 primary_technology, user_rating, year_of_payment,currency_type='LKR'):
        super().__init__(education_level, work_experience, designation, created_date_time, user_rating, no_of_employees)
        self.__salary_amount = salary_amount
        self.__primary_technology = primary_technology
        self.__year_of_payment = year_of_payment
        self.__currency_type = currency_type

    def get_salary_amount(self):
        return self.__salary_amount

    def set_salary_amount(self, salary_amount):
        self.__salary_amount = salary_amount

    def get_primary_technology(self):
        return self.__primary_technology

    def set_primary_technology(self, primary_technology):
        self.__primary_technology = primary_technology

    def get_year_of_payment(self):
        return self.__year_of_payment

    def set_year_of_payment(self, year_of_payment):
        self.__year_of_payment = year_of_payment

    def get_currency_type(self):
        return self.__currency_type

    def set_currency_type(self, currency_type):
        self.__currency_type = currency_type

    def __str__(self):
        return f"User Information: {super().__str__()} Salary: {self.__salary_amount} No. of Employees: " \
               f"{self.__no_of_employees} Primary Technology: {self.__primary_technology} "
