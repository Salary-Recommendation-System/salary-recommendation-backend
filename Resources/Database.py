from Resources.Config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine

db = SQLAlchemy()


class EncodedSalary(db.Model):
    __tablename__ = 'encoded_salary'
    __table_args__ = {'schema': 'recommendation'}

    id = db.Column(db.Integer, primary_key=True)
    education_level = db.Column(db.Integer)
    work_experience = db.Column(db.Integer)
    designation = db.Column(db.Integer)
    salary_amount = db.Column(db.Float)
    created_date_time = db.Column(db.DateTime, default=datetime.utcnow)
    no_of_employees = db.Column(db.Integer)


class RecommendationDetail(db.Model):
    __tablename__ = 'recommendation_details'
    __table_args__ = {'schema': 'recommendation'}

    id = db.Column(db.Integer, primary_key=True)
    education_level = db.Column(db.String(255))
    work_experience = db.Column(db.String(255))
    designation = db.Column(db.String(255))
    created_date_time = db.Column(db.DateTime, default=datetime.utcnow)
    salary_amount = db.Column(db.Numeric)
    no_of_employees = db.Column(db.String(255))
    user_rating = db.Column(db.Float)
    batch_id = db.Column(db.String)
    inflation_rate = db.Column(db.Float)
    inflation_amount = db.Column(db.Float)


class SalaryDetail(db.Model):
    __tablename__ = 'salary_details'
    __table_args__ = {'schema': 'recommendation'}

    id = db.Column(db.Integer, primary_key=True)
    education_level = db.Column(db.String(255))
    work_experience = db.Column(db.String(255))
    designation = db.Column(db.String(255))
    created_date_time = db.Column(db.DateTime, default=datetime.utcnow)
    salary_amount = db.Column(db.Numeric)
    no_of_employees = db.Column(db.String(255))
    primary_technology = db.Column(db.String(255))
    user_rating = db.Column(db.Float)
    year_of_payment = db.Column(db.Integer)


class EncodedSalaryConversion(db.Model):
    __tablename__ = 'encoded_salary_conversion'
    __table_args__ = {'schema': 'recommendation'}

    id = db.Column(db.Integer, primary_key=True)
    encoded_value = db.Column(db.Integer)
    unique_code = db.Column(db.String)


class Inflation(db.Model):
    __tablename__ = 'inflation'
    __table_args__ = {'schema': 'recommendation'}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.String)
    rate = db.Column(db.FLOAT)


def create_database_engine():
    config = Config()
    build_uri = f"postgresql://{config.get('user')}:{config.get('password')}@{config.get('host')}/{config.get('name')}"
    engine = create_engine(build_uri)
    return engine
