from . import GoogleFinState
from financials import CashItem

class ACashState(GoogleFinState):
    xpath='//div[@id="casannualdiv"]/table[@id="fs-table"]'

    def getItem(self):
        return CashItem()

    def insert(self, controller ,i):
        controller.insertGoogleAnnualCashFlow(i)

    def getTable(self):
        return "GoogleAnnualCashFlowStatements"

    def formatDate(self,date,i):
        split = date.split()
        i.insert("TimeSpan", split[0])
        i.insert("TimeUnit", split[1])
        i.insert("Date", split[3])

    def getFinancials(self, dic):
        return dic["ACash"]
