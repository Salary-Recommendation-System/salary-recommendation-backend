from abc import abstractmethod


class EncodedSalaryService:

    @abstractmethod
    def create(self, schema_name, encoded_table):
        pass

    @abstractmethod
    def save(self, encode_specific):
        pass

    @abstractmethod
    def get_encode_data(self, work_experience, education, company_size, designation):
        pass
