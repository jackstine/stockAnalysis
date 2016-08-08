import sys
sys.path.insert(1,"/home/jacob/Dropbox/Program/Stock/code/")
from pycharmCode.stock.datastructure import FinancialContainer
from . import GoogleFinState
from financials import BalanceItem

class ABalanceState(GoogleFinState):
    xpath='//div[@id="balannualdiv"]/table[@id="fs-table"]'

    def getItem(self):
        return BalanceItem()

    def insert(self, controller ,i):
        controller.insertGoogleAnnualBalanceSheet(i)

    def getTable(self):
        return "GoogleAnnualBalanceSheets";

    def formatDate(self,date,i):
        i.insert("Date",date.split()[2])

    def createFinancialContainer(self, el):
        return FinancialContainer(el["Symbol"] , el["Date"], None, None, el)

    def getFinancials(self, dic):
        return dic["ABalance"]
