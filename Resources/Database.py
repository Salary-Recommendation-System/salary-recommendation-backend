from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, String, Numeric


from Resources.connect_unix import get_connect_url

Base = declarative_base()


class EncodedSalary(Base):
    __tablename__ = 'encoded_salary'
    __table_args__ = {'schema': 'recommendation'}

    id = Column(Integer, primary_key=True)
    education_level = Column(Integer)
    work_experience = Column(Integer)
    designation = Column(Integer)
    salary_amount = Column(Float)
    created_date_time = Column(DateTime, default=datetime.utcnow)
    no_of_employees = Column(Integer)


class RecommendationDetail(Base):
    __tablename__ = 'recommendation_details'
    __table_args__ = {'schema': 'recommendation'}

    id = Column(Integer, primary_key=True)
    education_level = Column(String(255))
    work_experience = Column(String(255))
    designation = Column(String(255))
    created_date_time = Column(DateTime, default=datetime.utcnow)
    salary_amount = Column(Numeric)
    no_of_employees = Column(String(255))
    user_rating = Column(Float)
    batch_id = Column(String)


class SalaryDetail(Base):
    __tablename__ = 'salary_details'
    __table_args__ = {'schema': 'recommendation'}

    id = Column(Integer, primary_key=True)
    education_level = Column(String(255))
    work_experience = Column(String(255))
    designation = Column(String(255))
    created_date_time = Column(DateTime, default=datetime.utcnow)
    salary_amount = Column(Numeric)
    no_of_employees = Column(String(255))
    primary_technology = Column(String(255))
    user_rating = Column(Float)
    year_of_payment = Column(Integer)


class EncodedSalaryConversion(Base):
    __tablename__ = 'encoded_salary_conversion'
    __table_args__ = {'schema': 'recommendation'}

    id = Column(Integer, primary_key=True)
    encoded_value = Column(Integer)
    unique_code = Column(String)


def db_engine_connection():
    build_uri = get_connect_url()
    print(build_uri)
    engine = create_engine(build_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    return engine
