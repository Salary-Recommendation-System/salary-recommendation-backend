class Response:

    def __init__(self, code, message):
        self.__code = code
        self.__message = message

    def get_response(self):
        return {'message': self.__message, 'code': self.__code}

    def __str__(self):
        return f"Code: {self.__code}, Message: {self.__message}"
