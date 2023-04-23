import psycopg2
from Resources.Config import Config
import psycopg2.pool


class Database:
    def __init__(self):
        self.pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=18,
            database=Config.get('name'),
            user=Config.get('user'),
            password=Config.get('password'),
            host=Config.get('host')
        )

    def __enter__(self):
        self.conn = self.pool.getconn()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.pool.putconn(self.conn)
