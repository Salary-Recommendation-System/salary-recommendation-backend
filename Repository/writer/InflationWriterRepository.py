from Repository.InflationRepository import InflationRepository
from Resources.Database import Inflation
from Utils.Message import Message
from Utils.Response import Response


class InflationWriterRepository(InflationRepository):

    def update_inflation_rate(self, db_session, inflation):
        results = db_session.query(Inflation).filter(Inflation.year == inflation.get_year(),
                                                     Inflation.month == inflation.get_month()).all()
        if len(results) == 0:
            return Response(Message.NO_INFO_TO_UPDATE.value, Message.NO_INFO_TO_UPDATE.message)
        else:
            for result in results:
                result.rate = inflation.get_rate()
            db_session.commit()

        return Response(Message.SUCCESSFULLY_UPDATED_THE_INFLATION.value,
                        Message.SUCCESSFULLY_UPDATED_THE_INFLATION.message)

    def get_with_month_and_year(self, db_session, month, year):
        pass

    def get_latest_inflation(self, db_session):
        pass

    def save(self, db_session, inflation):
        try:
            inflation = Inflation(year=inflation.get_year(), month=inflation.get_month(), rate=inflation.get_rate())
            db_session.add(inflation)
            db_session.commit()

            return Response(Message.SUCCESS_MESSAGE.value, Message.SUCCESS_MESSAGE.message)
        except Exception as e:
            print(e)
            return Response(Message.DB_CONNECTION_FAILED.value, Message.DB_CONNECTION_FAILED.message)
