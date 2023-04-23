def save(education_level, work_experience, designation, created_date_time,
         user_rating, no_of_employees, recommendation, batch_id):
    return "INSERT INTO recommendation.recommendation_details(education_level, work_experience, designation, " \
           "created_date_time, salary_amount, no_of_employees, batch_id, user_rating)VALUES ( '{}','{}'," \
           "'{}','{}','{}','{}','{}','{}')".format(education_level, work_experience, designation,
                                                   created_date_time, float(recommendation), no_of_employees, batch_id,
                                                   user_rating)


def create(schema_name):
    return f'''
                        CREATE SCHEMA IF NOT EXISTS {schema_name};
                        CREATE TABLE {schema_name}.Recommendation_Details (
                            id SERIAL PRIMARY KEY,
                            education_level VARCHAR(255),
                            work_experience VARCHAR(255),
                            designation VARCHAR(255),
                            created_date_time TIMESTAMP,
                            salary_amount DECIMAL(10,2),
                            no_of_employees VARCHAR(255),
                            user_rating FLOAT,
                            batch_id VARCHAR
                        );
                    '''


