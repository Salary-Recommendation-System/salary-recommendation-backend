def get_all_information(work_experience, education, designation, no_of_employees):
    return "SELECT * FROM recommendation.salary_details WHERE work_experience='{}' AND education_level='{}' " \
           "AND designation = '{}' AND no_of_employees='{}'".format(work_experience, education, designation,
                                                                    no_of_employees)


def get_information(work_experience, education, designation, no_of_employees, amount):
    return "SELECT * FROM recommendation.salary_details WHERE work_experience='{}' AND education_level='{}' " \
           "AND designation = '{}' AND no_of_employees='{}' AND salary_amount='{}'".format(work_experience, education,
                                                                                           designation,
                                                                                           no_of_employees, amount)


def update_rating(rating, id):
    return "UPDATE recommendation.salary_details SET user_rating='{}' WHERE id = '{}'".format(float(rating), int(id))


def get_information_by_designation(designation):
    return "SELECT * FROM recommendation.salary_details WHERE designation = '{}'".format(designation)


def create(schema_name):
    return f'''
                    CREATE SCHEMA IF NOT EXISTS {schema_name};
                    CREATE TABLE {schema_name}.Salary_Details (
                        id SERIAL PRIMARY KEY,
                        education_level VARCHAR(255),
                        work_experience VARCHAR(255),
                        designation VARCHAR(255),
                        created_date_time TIMESTAMP,
                        salary_amount DECIMAL(10,2),
                        no_of_employees VARCHAR(255),
                        primary_technology VARCHAR(255),
                        user_rating FLOAT,
                        year_of_payment INT
                    );
                '''


def save(education_level, work_experience, designation, created_date_time, salary_amount, no_of_employees,
         primary_technology, user_rating, year_of_payment):
    return "INSERT INTO recommendation.salary_details(education_level, work_experience, designation, " \
           "created_date_time, salary_amount, no_of_employees, primary_technology, user_rating,year_of_payment)VALUES " \
           "( '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(education_level, work_experience, designation,
                                                                    created_date_time, salary_amount, no_of_employees,
                                                                    primary_technology, user_rating, year_of_payment)
