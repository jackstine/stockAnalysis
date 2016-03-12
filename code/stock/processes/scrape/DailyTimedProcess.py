from .. import Process
from ...commands import AmericanStockDailyThread, FinancialsThread,DailyInformationThread
from ...utility import Time
from ...repository.process import ProcessCompletesRepo
from ...streams.mysql import DB

#*****NON_CLASS_METHODS******#
def sleepClosedMarket(self):
    Time.sleepWeekendOrUntil(self.NASDAQ_SCRAPING_TIME_UTC, Time.today())

def sleepDaily(self):
    Time.tillNextDay()

class DailyTimedProcess(Process):
    start = None
    count = 0
    NASDAQ_TIME_UTC = Time.t(hours = 14, minutes = 30)      # 9:30 EST
    NASDAQ_SCRAPING_TIME_UTC = Time.t(hours = 22, minutes = 0)  # 5 EST
    AMERICAN_STOCKS = {"Name":"AmericanStocks", "CompletesRepo":"AmericanStockCompletes", 
        "Thread":AmericanStockDailyThread,"Sleep":sleepClosedMarket}
    DAILY_INFO = {"Name":"Commodities", "CompletesRepo":"CommoditiesCompletes",
        "Thread":DailyInformationThread,"Sleep":sleepDaily}
    FINANCIAL = {"Name":"Financial Gather", "FinancialCompletes":"FinancialCompletes",
        "Thread":FinancialsThread,"Sleep":sleepClosedMarket}

    def __init__(self, options):
        Process.__init__(self, options["Name"])
        self.repo = ProcessCompletesRepo(options["CompletesRepo"])
        self.mysql = DB(DB.Connections.STOCK)
        self.options = options

    def createProcess(self):
        self.start = Time.today()
        return self.options["Thread"]()

    def onStop(self):
        self.mysql.close()

    def timeSync(self):
        self.insertTime()
        self.mysql.close()
        self.clearStartTime()
        self.options["Sleep"](self)
        self.mysql = DB(DB.Connections.STOCK)

    def insertTime(self):
        if (self.start != None):
            model = InsertModel(self.repo.table)
            model.insert("day", self.start)
            self.mysql.insert(model).execute()

    def clearStartTime(self):
        self.start = None
