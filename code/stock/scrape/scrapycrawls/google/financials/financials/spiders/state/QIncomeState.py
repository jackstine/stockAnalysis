from . import GoogleFinState
from financials import IncomeItem

class QIncomeState(GoogleFinState):
    xpath='//div[@id="incinterimdiv"]/table[@id="fs-table"]'

    def getItem(self):
        return IncomeItem()

    def insert(self, controller, i):
        controller.insertGoogleQuarterlyIncomeStatement(i)

    def getTable(self):
        return "GoogleQuarterlyIncomeStatements"

    def formatDate(self,date,i):
        split = date.split()
        i.insert("TimeSpan", split[0])
        i.insert("TimeUnit", split[1])
        i.insert("Date", split[3])

    def getFinancials(self, dic):
        return dic["QIncome"]
