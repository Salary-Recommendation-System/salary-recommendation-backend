from sqlalchemy.exc import SQLAlchemyError

from Domain.InflationCal import InflationCal
from Repository.InflationRepository import InflationRepository
from Resources.Database import Inflation
from Utils.Response import Response
from Utils.Scripts.InflationQueryUtil import get_latest_inflation
from sqlalchemy import text


class InflationReaderRepository(InflationRepository):

    def update_inflation_rate(self, db_session, inflation):
        pass

    def get_with_month_and_year(self, db_session, month, year):
        result = db_session.query(Inflation.id, Inflation.year, Inflation.month, Inflation.rate) \
            .filter(Inflation.year == year, Inflation.month == month.capitalize()) \
            .order_by(Inflation.year, Inflation.month).all()
        if len(result) == 0:
            return False
        else:
            return True

    def save(self, db_session, inflation):
        pass

    def get_latest_inflation(self, db_session):
        try:

            data = db_session.execute(text(get_latest_inflation()))
            rows = data.fetchall()

            inflation = []

            for row in rows:
                inflation.append(InflationCal(row[1],row[2],row[3]))

            return inflation
        except SQLAlchemyError as e:
            print(e)
            db_session.rollback()
        except Exception as e:
            print(e)
            return Response(e, 400)
