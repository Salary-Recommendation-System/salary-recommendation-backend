def save(rating_information):
    return "INSERT INTO recommendation.encoded_salary(education_level, work_experience, designation, " \
           "created_date_time, salary_amount, no_of_employees) " \
           "VALUES ('{}','{}','{}','{}','{}','{}')".format(int(rating_information.get_education_level()),
                                                           int(rating_information.get_work_experience()),
                                                           int(rating_information.get_designation()),
                                                           rating_information.get_created_date_time(),
                                                           float(rating_information.get_salary_amount()),
                                                           int(rating_information.get_no_of_employees()))


def create_encode_table_with_user_inputs(schema_name):
    return f'''
                        CREATE SCHEMA IF NOT EXISTS {schema_name};
                        CREATE TABLE {schema_name}.Encoded_Salary_Conversion (
                            id SERIAL PRIMARY KEY,
                            encoded_value INT,
                            unique_code VARCHAR
                        );
                    '''


def save_encode_data(encode_data, code):
    return "INSERT INTO recommendation.encoded_salary_conversion(encoded_value, unique_code) VALUES ('{}','{}')" \
        .format(int(encode_data), code)


def get_based_on_parameters(work_experience, education, company_size, designation):
    return "SELECT * FROM recommendation.encoded_salary_conversion WHERE unique_code in ('{}','{}','{}','{}')".format(
        work_experience, education, company_size, designation
    )
