from abc import abstractmethod


class RecommendationRepository:

    @abstractmethod
    def save(self,db_session, recommendation_user):
        pass

