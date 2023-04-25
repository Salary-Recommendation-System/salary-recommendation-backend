import jsons
from flask import Flask, jsonify, request, Blueprint

from Domain.InformationUser import InformationUser
from Domain.RecommendationUser import RecommendationUser
from Resources.Database import db
from ServiceImplementation.EncodedSalaryServiceImpl import EncodedSalaryServiceImpl
from ServiceImplementation.GetRecommendationServiceImpl import GetRecommendationServiceImpl
from ServiceImplementation.SaveSalaryInformationServiceImpl import SaveSalaryInformationServiceImpl
from datetime import datetime


bp = Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route("/")
def load():
    return jsonify('{message: hello}'), 200


@bp.route('/save_info', methods=['POST'])
def save_salary_information_api():
    # Accessing the json request
    data = request.get_json()
    save_existing_data = request.args.get('saved_existing_data')

    saving_data_obj = SaveSalaryInformationServiceImpl()
    if save_existing_data == 'TRUE':
        created_response = saving_data_obj.save_existing_data(db.session)
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

        saved_response = saving_data_obj.save(db.session, information_user)
        response = jsons.dump(saved_response)
        return jsonify(response), 200


@bp.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.get_json()

    education_level = data['_education_level']
    work_experience = data['_work_experience']
    designation = data['_designation']
    no_of_employees = data['_no_of_employees']

    recommendation_system = RecommendationUser(education_level, work_experience, designation, datetime.now(), 0.0,
                                               no_of_employees, "")
    get_recommendation_result = GetRecommendationServiceImpl()
    created_response = get_recommendation_result.save(db.session, recommendation_system)
    print(created_response)
    response = jsons.dump(created_response)
    return jsonify(response), 200


@bp.route('/rating/<id>', methods=['PUT'])
def update_rating(id):
    rating = request.args.get('rating')
    service = SaveSalaryInformationServiceImpl()
    created_response = service.update_rating(db.session, int(rating), int(id))

    response = jsons.dump(created_response)
    return jsonify(response), 200


@bp.route('/encoded', methods=['POST'])
def save_encoded_salary():
    encode_specific = request.args.get('encode_specific')
    save = EncodedSalaryServiceImpl()
    if encode_specific == 'YES':
        created_response = save.save(db.session, True)
    else:
        created_response = save.save(db.session, False)

    response = jsons.dump(created_response)
    return jsonify(response), 200
