import os

import jsons
from flask import Flask, jsonify, request

from Domain.InformationUser import InformationUser
from Domain.RecommendationUser import RecommendationUser
from ServiceImplementation.EncodedSalaryServiceImpl import EncodedSalaryServiceImpl
from ServiceImplementation.GetRecommendationServiceImpl import GetRecommendationServiceImpl
from ServiceImplementation.SaveSalaryInformationServiceImpl import SaveSalaryInformationServiceImpl
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def load():
    return jsonify('{message: hello}'), 200


@app.route('/api/v1/save_info', methods=['POST'])
def save_salary_information_api():
    # Accessing the json request
    data = request.get_json()
    save_existing_data = request.args.get('saved_existing_data')

    saving_data_obj = SaveSalaryInformationServiceImpl()
    if save_existing_data == 'TRUE':
        created_response = saving_data_obj.save_existing_data()
        response = jsons.dump(created_response)
        return jsonify(response), 200
    else:
        # Converting the json request to the Object
        education_level = data['_education_level']
        work_experience = data['_work_experience']
        designation = data['_designation']
        created_date_time = datetime.now()
        salary_amount = data['_salary_amount']
        no_of_employees = data['_no_of_employees']
        primary_technology = data['_primary_technology']
        user_rating = data['_user_rating']
        year_payment = data['_year_of_pay']
        currency_type = data['_currency_type']

        information_user = InformationUser(education_level, work_experience, designation, created_date_time,
                                           float(salary_amount), no_of_employees, primary_technology,
                                           float(user_rating),
                                           int(year_payment), currency_type)

        saved_response = saving_data_obj.save(information_user)
        response = jsons.dump(saved_response)
        return jsonify(response), 200


@app.route('/api/v1/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.get_json()

    education_level = data['_education_level']
    work_experience = data['_work_experience']
    designation = data['_designation']
    no_of_employees = data['_no_of_employees']

    recommendation_system = RecommendationUser(education_level, work_experience, designation, datetime.now(), 0.0,
                                               no_of_employees, "")
    get_recommendation_result = GetRecommendationServiceImpl()
    created_response = get_recommendation_result.save(recommendation_system)
    response = jsons.dump(created_response)
    return jsonify(response), 200


@app.route('/api/v1/rating/<id>', methods=['PUT'])
def update_rating(id):
    rating = request.args.get('rating')
    service = SaveSalaryInformationServiceImpl()
    created_response = service.update_rating( int(rating), int(id))

    response = jsons.dump(created_response)
    return jsonify(response), 200


@app.route('/api/v1/encoded', methods=['POST'])
def save_encoded_salary():
    encode_specific = request.args.get('encode_specific')
    save = EncodedSalaryServiceImpl()
    created_response = save.save(bool(encode_specific))
    response = jsons.dump(created_response)
    return jsonify(response), 200


@app.route('/api/v1/create_table/<schema_name>', methods=['GET'])
def create_table(schema_name):
    # Getting the query parameter
    information_provider = request.args.get('information_provider')
    encode = request.args.get('encode_conversion')

    if information_provider == 'YES':
        create_table_for_save_salary_information = SaveSalaryInformationServiceImpl()
        created_response = create_table_for_save_salary_information.create(schema_name)
        response = jsons.dump(created_response)
        return jsonify(response), 200
    elif information_provider == 'NO':
        create_table_for_recommendation_user = GetRecommendationServiceImpl()
        created_response = create_table_for_recommendation_user.create(schema_name)
        response = jsons.dump(created_response)
        return jsonify(response), 200
    elif information_provider == 'ENCODE_DATA':
        create_table_for_encode_details = EncodedSalaryServiceImpl()

        if bool(encode):
            created_response = create_table_for_encode_details.create(schema_name, True)
        else:
            created_response = create_table_for_encode_details.create(schema_name, False)

        response = jsons.dump(created_response)
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
