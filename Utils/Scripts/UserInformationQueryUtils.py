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
