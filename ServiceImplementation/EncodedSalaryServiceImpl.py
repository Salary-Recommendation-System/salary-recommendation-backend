from Repository.Reader.EncodedSalaryReaderRepository import EncodedSalaryReaderRepository
from Repository.writer.EncodedSalaryWriterRepository import EncodedSalaryWriterRepository
from Service.EncodedSalaryService import EncodedSalaryService
import pandas as pd
from Utils.Message import Message

from Utils.Response import Response


class EncodedSalaryServiceImpl(EncodedSalaryService):

    def get_encode_data(self,db_session, work_experience, education, company_size, designation):
        encoded_reader_repository = EncodedSalaryReaderRepository()
        return encoded_reader_repository.get_encode_data(db_session,work_experience, education, company_size,
                                                         designation)

    def save(self,db_session, encode_specific):
        try:
            encoded_writer_repository = EncodedSalaryWriterRepository()

            if bool(encode_specific):
                data = pd.read_csv("Utils/Files/encoded_data.csv")
                return encoded_writer_repository.save_encode_data(db_session,data)
            else:
                data = pd.read_csv("Utils/Files/encoded.csv")
                return encoded_writer_repository.save(db_session,data)
        except Exception as e:
            print(e)
            return Response(Message.ENCODED_FILE_NOT_AVAILABLE.value, Message.ENCODED_FILE_NOT_AVAILABLE.message)
