import uuid
from datetime import datetime

import psycopg2.errors

from Repository.RecommendationRepository import RecommendationRepository
from Resources.Database import Database
from Utils.Message import Message
from Utils.Response import Response
from Utils.Scripts import RecommendationQueryUtils


class RecommendationWriterRepository(RecommendationRepository):

    def save(self, recommendation_user):
        uniqueid = uuid.uuid1()
        try:
            with Database() as database:
                for key, values in recommendation_user.get_recommendation().items():
                    for item in values:
                        save_query = RecommendationQueryUtils.save(item['education_level'], item['work_experience'],
                                                                   item['designation'], datetime.now(), item['user_rating'],
                                                                   item['no_of_employees'], item['salary_amount'], uniqueid)
                        database.cursor.execute(save_query)
            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except psycopg2.errors.DuplicateTable:
            return Response(Message.DB_TABLE_ALREADY_CREATED.value, Message.DB_TABLE_ALREADY_CREATED.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)

    def create(self, schema_name):
        try:
            with Database() as database:

                create_query = RecommendationQueryUtils.create(schema_name)
                database.cursor.execute(create_query)
            return Response(Message.DB_TABLE_CREATED.value, Message.DB_TABLE_CREATED.message)
        except psycopg2.errors.DuplicateTable:
            return Response(Message.DB_TABLE_ALREADY_CREATED.value, Message.DB_TABLE_ALREADY_CREATED.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
