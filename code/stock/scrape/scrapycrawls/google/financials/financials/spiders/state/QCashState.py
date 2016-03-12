from . import GoogleFinState
from financials import CashItem

class QCashState(GoogleFinState):
    xpath='//div[@id="casinterimdiv"]/table[@id="fs-table"]'

    def getItem(self):
        return CashItem()

    def insert(self, controller ,i):
        controller.insertGoogleQuarterlyCashFlow(i)

    def getTable(self):
        return "GoogleQuarterlyCashFlowStatements"

    def formatDate(self,date,i):
        split = date.split()
        i.insert("TimeSpan", split[0])
        i.insert("TimeUnit", split[1])
        i.insert("Date", split[3])

    def getFinancials(self, dic):
        return dic["QCash"]
