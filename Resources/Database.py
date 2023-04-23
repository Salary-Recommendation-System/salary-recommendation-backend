import os

import pymysql.cursors

from Resources.Config import Config
from Utils.Response import Response

config = Config()
db_user = config.get('user')
db_password = config.get('password')
db_name = config.get('name')
db_host = config.get('host')


def open_connection():
    unix_socket = '/cloudsql/{}'.format("salary-recommendation-system:asia-south2:database")
    try:
        conn = pymysql.connect(user=db_user,
                               password=db_password,
                               db=db_name,
                               cursorclass=pymysql.cursors.DictCursor,
                               host=db_host
                               )
        return conn
    except pymysql.MySQLError as e:
        print(e)
        return Response(400, "DB SQL error")
