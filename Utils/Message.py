from enum import Enum


class Message(Enum):

    def __init__(self, message, value):
        self.__message = message
        self.__value = value

    @property
    def message(self):
        return self.__message

    @property
    def value(self):
        return self.__value

    SUCCESS_MESSAGE = ("Successfully saved information", 200)
    SALARY = ("Salary amount is incorrect please check on it", 400)
    NO_OF_EMPLOYEES = ("Please specify the employees amount that the company which you worked at", 400)
    PRIMARY_TECHNOLOGY = ("Specify which technology that you were expert in", 400)
    DB_CONNECTION_FAILED = ("Database Connection was not able to be connected", 503)
    DB_CONNECTION_SUCCESSFUL = ("Database has been connected Successfully", 200)
    DB_TABLE_CREATED = ("The table has been created successfully", 201)
    DB_TABLE_ALREADY_CREATED = ("The table has already been created ", 409)
    SAVING_FAILED = ("Failed to save information", 400)
    INFORMATION_ALREADY_EXIST = ("Information already exists", 412)
    FAILED_TO_UPDATE_WITH_EXCEL_ID = ("Failed to update with excel_id", 404)
    SUCCESSFULLY_UPDATED_WITH_EXCEL_ID = ("Successfully updated with excel_id", 200)
    FAILED_TO_GET_RATING_INFORMATION = ("Failed to get rating information", 404)
    FAILED_TO_GET_RATING_WITH_EXCEL_ID = ("Failed to get rating information with excel id", 404)
    INFORMATION_NOT_AVAILABLE_TO_UPDATE = ("The information is not available", 404)
    SUCCESSFULLY_UPDATED_WITH_INFORMATION = ("Successfully updated the rating", 200)
    ENCODED_FILE_NOT_AVAILABLE = ("Encoded file not available", 404)
    UNIQUE_SALARY_FILE_NOT_FOUND = ("Salary file not available", 404)
    INDEX_ACCESS_FAILURE = ("The access of index is failed please check the DB return", 404)
