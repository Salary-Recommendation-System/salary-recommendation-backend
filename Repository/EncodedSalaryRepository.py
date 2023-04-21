from abc import abstractmethod


class EncodedSalaryRepository:

    @abstractmethod
    def save(self,db_session, encode_information):
        pass

    @abstractmethod
    def save_encode_data(self,db_session, binary_information):
        pass

    @abstractmethod
    def get_encode_data(self,db_session, work_experience, education, company_size, designation):
        pass
