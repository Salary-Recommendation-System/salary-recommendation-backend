import uuid
from datetime import datetime
from Repository.RecommendationRepository import RecommendationRepository
from Resources.Database import open_connection
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import RecommendationQueryUtils


class RecommendationWriterRepository(RecommendationRepository):

    def save(self, recommendation_user):
        uniqueid = uuid.uuid1()
        try:
            with open_connection().cursor() as cursor:
                for key, values in recommendation_user.get_recommendation().items():
                    for item in values:
                        save_query = RecommendationQueryUtils.save(str(item['education_level']),
                                                                   str(item['work_experience']),
                                                                   str(item['designation']), datetime.now(),
                                                                   int(item['user_rating']),
                                                                   str(item['no_of_employees']),
                                                                   float(item['salary_amount']), uniqueid)
                        cursor.execute(save_query)
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def create(self, schema_name):
        try:
            with open_connection().cursor() as cursor:
                create_query = RecommendationQueryUtils.create(schema_name)
                cursor.execute(create_query)
            return Response(Message.DB_TABLE_CREATED.value, Message.DB_TABLE_CREATED.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
