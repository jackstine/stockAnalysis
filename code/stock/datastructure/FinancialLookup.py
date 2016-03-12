from . import FinancialContainerList

class FinancialLookup:
	"""This is a list that contains FinancialContainerLists
	easy allows for lookup for a symbol
	The list that it INIT is sorted then put into lookup tables
	the list MUST be of class FinancialContainer
	"""

	def __init__(self,theList):
		sortedList = sorted(theList)
		self._configureList(sortedList)

	def _configureList(self,sortedList):
		"""Creates the LookUp Table 
		"""
		symNum = 0
		if ( len(sortedList) == 0):
			self.financialList = None
		else:
			currentSymbol = sortedList[0].symbol
			self.financialList = []
			self.financialList.append( FinancialContainerList(currentSymbol) )
			for el in sortedList:
				if (el.symbol == currentSymbol):
					self.financialList[ symNum ].append(el)
				else:
					symNum += 1
					currentSymbol = el.symbol
					self.financialList.append(FinancialContainerList(currentSymbol))
					self.financialList[ symNum ].append(el)

	def getList(self, symbol):
		"""Searches the list of financialList elements and finds the
		symbol list corresponding to the lookup
		"""
		if self.financialList == None:
			return None
		for el in self.financialList:
			if ( el.symbol == symbol):
				return el.getList()
		#TODO create a error flag here
