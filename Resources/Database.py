import psycopg2 as psycopg2

from Domain.VO.DbConnection import DBConnection
from configparser import ConfigParser

from Resources.Config import Config


def db_connection():
    config = Config()
    conn = psycopg2.connect(database=config.get('name'), user=config.get('user'), password=config.get('password'),
                            host=config.get('host'))
    cursor = conn.cursor()
    return DBConnection(conn, cursor)


def get_configurations():
    pass
