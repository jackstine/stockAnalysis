class FinancialContainerList:
	"""A data structure that contains the symbol and the list of items
	"""
	def __init__(self,symbol):
		self.symbol = symbol
		self.List = []

	def append(self, el):
		self.List.append(el)

	def getList(self):
		return self.List
