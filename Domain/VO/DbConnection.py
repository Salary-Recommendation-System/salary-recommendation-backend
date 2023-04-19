class DBConnection:

    def __init__(self, connection, cursor):
        self.__connection = connection
        self.__cursor = cursor

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor
