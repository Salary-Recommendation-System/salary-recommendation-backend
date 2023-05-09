from abc import abstractmethod


class InflationRepository:

    @abstractmethod
    def save(self, db_session, inflation):
        pass

    @abstractmethod
    def get_latest_inflation(self, db_session):
        pass

    @abstractmethod
    def get_with_month_and_year(self, db_session, month, year):
        pass

    @abstractmethod
    def update_inflation_rate(self, db_session,inflation):
        pass
