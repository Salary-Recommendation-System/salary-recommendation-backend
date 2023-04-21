def save(education_level, work_experience, designation, created_date_time,
         user_rating, no_of_employees, recommendation, batch_id):
    return "INSERT INTO recommendation.recommendation_details(education_level, work_experience, designation, " \
           "created_date_time, salary_amount, no_of_employees, batch_id, user_rating)VALUES ( '{}','{}'," \
           "'{}','{}','{}','{}','{}','{}')".format(education_level, work_experience, designation,
                                                   created_date_time, float(recommendation), no_of_employees, batch_id,
                                                   user_rating)
