PRICE = "quote"
ADJUSTED_PRICE = "adjustPrice"
DATE = "date"
RATIO = "ratio"
MAX_RETURN = "max_return"
MAX_LOSS = "max_loss"
ANNULALIZED_MAX_RETURN = "annulalized_max_return"
ANNULALIZED_MAX_LOSS = "annulalized_max_loss"
SHORT = "short"
ANNULALIZED_SHORT = "annulalized_short"
LONG = "long"
ANNULALIZED_LONG = "annulalized_long"


ONE_WEEK = 5
ONE_MONTH = 22
TWO_MONTHS = 44
ONE_QUARTER = 66
TWO_QUARTERS = ONE_QUARTER * 2
THREE_QUARTERS = TWO_QUARTERS + ONE_QUARTER
ONE_YEAR = TWO_QUARTERS * 2
ONE_HALF_YEAR = ONE_YEAR + TWO_QUARTERS
TWO_YEARS = ONE_YEAR * 2
THREE_YEARS = TWO_YEARS + ONE_YEAR
FOUR_YEARS = TWO_YEARS * 2
FIVE_YEARS = ONE_YEAR * 5
SIX_YEARS = ONE_YEAR * 6
SEVEN_YEARS = ONE_YEAR * 7
EIGHT_YEARS = ONE_YEAR * 8
NINE_YEARS = ONE_YEAR * 9
TEN_YEARS = ONE_YEAR * 10
TERM = "term"
YEARS = "years"
TERMS = {"week_1":{TERM:ONE_WEEK, YEARS:1},"month_1":{TERM:ONE_MONTH, YEARS:1},"months_2":{TERM:TWO_MONTHS, YEARS:1},"quarter_1": {TERM:ONE_QUARTER, YEARS:1},
    "quarters_2":{TERM:TWO_QUARTERS, YEARS:1}, "quarters_3":{TERM:THREE_QUARTERS, YEARS:1}
    ,"year_1":{TERM:ONE_YEAR, YEARS:1}, "quarters_6":{TERM:ONE_HALF_YEAR, YEARS:1}, "years_2":{TERM:TWO_YEARS, YEARS:2},
    "years_3":{TERM:THREE_YEARS, YEARS:3}, "years_4":{TERM:FOUR_YEARS, YEARS:4}, "years_5":{TERM:FIVE_YEARS, YEARS:5}
    ,"years_6":{TERM:SIX_YEARS, YEARS:6}, "years_7":{TERM:SEVEN_YEARS, YEARS:7},
    "years_8":{TERM:EIGHT_YEARS, YEARS:8},"years_9":{TERM:NINE_YEARS, YEARS:9},"years_10":{TERM:TEN_YEARS, YEARS:10}}

class PriceStructure:
    def __init__(self):
        self.prices = None
        self.startDate = None
        self.endDate = None
        self.startPrice = 0
        self.endPrice = 0
        self.returnValue = 0
        self.annulized_return = 0
        self.term = "" #tells us the term that is used
        self.type = ""#tells us if it is a Short or Long

    def setPrices(self,prices):
        self.prices = prices
    def setStartDate(self, date):
        self.startDate = date
    def setEndDate(self, date):
        self.endDate = date
    def setStartPrice(self, price):
        self.startPrice = price
    def setEndPrice(self, price):
        self.endPrice = price
    def setReturn(self,returnValue):
        self.returnValue = returnValue
    def setAnnualizedReturn(self,annual):
        self.annulized_return = annual
    def setTerm(self,term):
        self.term = term
    def setType(self,type):
        self.type = type

class PriceDateTime:
    def __init__(self):
        self.prices = None
        self.dates = None
    def setPrices(self, prices):
        self.prices = prices
        self.dates = prices.index.tolist()
    def getPricesAt(self,index):
        return self.prices[index]
    def getDateAt(self,index):
        return self.dates[index]