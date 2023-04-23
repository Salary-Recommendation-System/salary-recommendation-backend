from abc import abstractmethod


class EncodedSalaryRepository:

    @abstractmethod
    def create(self, schema_name, encoded_table):
        pass

    @abstractmethod
    def save(self, encode_information):
        pass

    @abstractmethod
    def save_encode_data(self, binary_information):
        pass

    @abstractmethod
    def get_encode_data(self, work_experience, education, company_size, designation):
        pass
