from abc import abstractmethod


class GetRecommendationService:

    @abstractmethod
    def save(self,db_session, recommendation_user):
        pass
