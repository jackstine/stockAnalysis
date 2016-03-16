from . import GoogleFinState
from financials import IncomeItem

class AIncomeState(GoogleFinState):
    xpath='//div[@id="incannualdiv"]/table[@id="fs-table"]'

    def getItem(self):
        return IncomeItem()

    def getTable(self):
        return "GoogleAnnualIncomeStatements"

    def formatDate(self,date,i):
        split = date.split()
        i.insert("TimeSpan", split[0])
        i.insert("TimeUnit", split[1])
        i.insert("Date", split[3])

    def getFinancials(self, dic):
        return dic["AIncome"]
