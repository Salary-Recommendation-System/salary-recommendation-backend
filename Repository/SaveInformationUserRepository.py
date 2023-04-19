from abc import abstractmethod


class SaveInformationUserRepository:

    @abstractmethod
    def save(self, information_user):
        pass

    @abstractmethod
    def create(self, schema_name):
        pass

    @abstractmethod
    def save_from_excel(self, information):
        pass

    @abstractmethod
    def get_all_saved_information(self, work_experience, education, designation, no_of_employees,amount):
        pass

    @abstractmethod
    def update_rating(self,rating,id):
        pass
