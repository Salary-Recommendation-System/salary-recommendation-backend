from abc import abstractmethod


class RecommendationRepository:

    @abstractmethod
    def save(self, recommendation_user):
        pass

    @abstractmethod
    def create(self, schema_name):
        pass
