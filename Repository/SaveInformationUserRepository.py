from abc import abstractmethod


class SaveInformationUserRepository:

    @abstractmethod
    def save(self,db_session, information_user):
        pass

    @abstractmethod
    def save_from_excel(self,db_session, information):
        pass

    @abstractmethod
    def get_all_saved_information(self,db_session, work_experience, education, designation, no_of_employees,amount):
        pass

    @abstractmethod
    def update_rating(self,db_session,rating,id):
        pass
