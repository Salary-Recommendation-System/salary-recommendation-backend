from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

from Repository.SaveInformationUserRepository import SaveInformationUserRepository
from Resources.Database import SalaryDetail, create_database_engine
from Utils.Message import Message
from Utils.Response import Response
import pandas as pd

engine = create_database_engine()


class SaveInformationUserReaderRepository(SaveInformationUserRepository):

    def get_all_saved_information(self, db_session, work_experience, education, designation, no_of_employees, amount):
        try:
            if amount is None:
                try:
                    filters = [
                        SalaryDetail.work_experience == str(work_experience),
                        SalaryDetail.education_level == str(education),
                        SalaryDetail.designation == str(designation),
                        SalaryDetail.no_of_employees == str(no_of_employees)

                    ]

                    query = db_session.query(SalaryDetail).filter(*filters).order_by(desc(SalaryDetail.user_rating))

                    result = engine.connect().execute(query.statement)

                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())

                    if dataframe.empty:
                        query = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation))\
                            .order_by(desc(SalaryDetail.user_rating))
                        result = engine.connect().execute(query.statement)
                        # Convert the result to a Pandas DataFrame
                        dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())
                        engine.dispose()
                        return dataframe
                    engine.dispose()
                    return dataframe
                except Exception as e:
                    print(e)
                    query = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation))\
                        .order_by(desc(SalaryDetail.user_rating))
                    result = engine.connect().execute(query.statement)
                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())

                    if dataframe.empty:
                        query = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation))\
                            .order_by(desc(SalaryDetail.user_rating))
                        result = engine.connect().execute(query.statement)
                        # Convert the result to a Pandas DataFrame
                        dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())
                        engine.dispose()
                        return dataframe
                    # Return the DataFrame
                    engine.dispose()
                    return dataframe

            else:
                try:

                    filters = [
                        SalaryDetail.work_experience == str(work_experience),
                        SalaryDetail.education_level == str(education),
                        SalaryDetail.designation == str(designation),
                        SalaryDetail.no_of_employees == str(no_of_employees),
                        SalaryDetail.salary_amount == float(amount)
                    ]
                    query = db_session.query(SalaryDetail).filter(*filters)\
                        .order_by(desc(SalaryDetail.user_rating))
                    result = engine.connect().execute(query.statement)

                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())
                    engine.dispose()
                    return dataframe
                except Exception as e:
                    print(e)
                    query = db_session.query(SalaryDetail).filter(SalaryDetail.designation == str(designation)) \
                        .order_by(desc(SalaryDetail.user_rating))
                    result = engine.connect().execute(query.statement)
                    # Convert the result to a Pandas DataFrame
                    dataframe = pd.DataFrame(result.fetchall(), columns=result.keys())
                    engine.dispose()
                    return dataframe

        except SQLAlchemyError as e:
            db_session.rollback()
        except Exception as e:
            print(e)
            return Response(e, 400)

    def save(self, db_session, information_user):
        pass

    def create(self, db_session, schema_name):
        pass

    def save_from_excel(self, db_session, information):
        pass

    def update_rating(self, db_session, rating, id):
        pass
