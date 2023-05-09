from Repository.Reader.InflationReaderRepository import InflationReaderRepository
from Repository.writer.InflationWriterRepository import InflationWriterRepository
from Service.InflationService import InflationService
import calendar

from Utils.Message import Message
from Utils.Response import Response


class InflationServiceImpl(InflationService):

    def get_inflation(self,db_session):
        reader_repository = InflationReaderRepository()
        result = reader_repository.get_latest_inflation(db_session)

        # Inflation calculation
        # Returns the latest and then the last months
        # Inflation rate calculation
        # Inflation rate = ((CPI in latest - CPI in past) / CPI in past) * 100%
        if len(result) == 0:
            return []
        else:
            inflation_rate = ((result[0].get_rate() - result[1].get_rate()) / result[1].get_rate()) * 100
            return [1 + (inflation_rate/100)]

    def save(self, db_session, inflation):

        try:

            if inflation.get_month().capitalize() in calendar.month_name[1:]:
                reader_repository = InflationReaderRepository()
                writer_repository = InflationWriterRepository()
                if not reader_repository.get_with_month_and_year(db_session, inflation.get_month().upper(),
                                                                 inflation.get_year()):
                    return writer_repository.save(db_session, inflation)
                else:
                    return writer_repository.update_inflation_rate(db_session, inflation)
            else:
                return Response(Message.MONTH_NOT_FOUND.value, Message.MONTH_NOT_FOUND.message)

        except Exception as e:
            print(e)
