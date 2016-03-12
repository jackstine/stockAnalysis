import sys
sys.path.insert(1,"/home/jacob/Dropbox/Program/Stock/code/")
from stock.datastructure import FinancialContainer

class GoogleFinState:
	xpath=""

	def getItem(self):
		pass

	def insert(self, controller, i):
		pass

	def formatDate(self, date):
		pass

	def createFinancialContainer(self, el):
		return FinancialContainer(el["Symbol"] , el["Date"], el["TimeSpan"], el["TimeUnit"], el)

	def getFinancials(self, dic):
		pass
