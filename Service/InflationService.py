from abc import abstractmethod


class InflationService:

    @abstractmethod
    def save(self,db_session, inflation):
        pass

    @abstractmethod
    def get_inflation(self,db_session):
        pass
