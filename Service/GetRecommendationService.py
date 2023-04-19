from abc import abstractmethod


class GetRecommendationService:
    
    @abstractmethod
    def create(self, schema_name):
        pass

    @abstractmethod
    def save(self, recommendation_user):
        pass
