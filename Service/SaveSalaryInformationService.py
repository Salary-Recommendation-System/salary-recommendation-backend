from abc import abstractmethod


class SaveSalaryInformationService:

    @abstractmethod
    def create(self, schema_name):
        pass

    @abstractmethod
    def save(self, information_user):
        pass

    @abstractmethod
    def save_existing_data(self):
        pass

    @abstractmethod
    def update_rating(self, rating, id):
        pass
