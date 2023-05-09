class InflationCal:
    def __init__(self, year, month, rate):
        self.__year = year
        self.__month = month
        self.__rate = rate

    # Getter for year
    def get_year(self):
        return self.__year

    # Setter for year
    def set_year(self, year):
        self.__year = year

    # Getter for month
    def get_month(self):
        return self.__month

    # Setter for month
    def set_month(self, month):
        self.__month = month

    # Getter for rate
    def get_rate(self):
        return self.__rate

    # Setter for rate
    def set_rate(self, rate):
        self.__rate = rate


