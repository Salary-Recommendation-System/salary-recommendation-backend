from abc import abstractmethod


class EncodedSalaryService:

    @abstractmethod
    def save(self,db_session, encode_specific):
        pass

    @abstractmethod
    def get_encode_data(self,db_session, work_experience, education, company_size, designation):
        pass
