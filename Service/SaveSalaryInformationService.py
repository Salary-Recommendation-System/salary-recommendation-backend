from abc import abstractmethod


class SaveSalaryInformationService:

    @abstractmethod
    def save(self,db_session, information_user):
        pass

    @abstractmethod
    def save_existing_data(self,db_session):
        pass

    @abstractmethod
    def update_rating(self,db_session,rating, id):
        pass
