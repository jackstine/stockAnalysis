class FinancialContainer:
	
	def __init__(self,symbol,date,timeSpan,timeUnit,data):
		self.symbol=symbol
		self.date= str(date)
		self.timeSpan= str(timeSpan)
		self.timeUnit=timeUnit
		self.data=data

	def __str__(self):
		return str( self.symbol+"  "+ str(self.date) +"  "+ str(self.timeSpan) +"  " + str(self.timeUnit) )

	def __hash__(self):
		return str(self).__hash__()

	def getWeeks(self):
		weeks=0
		if self.timeUnit=="months":
			weeks = 4*self.timeSpan
		elif self.timeUnit=="weeks":
			weeks=self.timeSpan
		return weeks
		
	def __eq__(self,other):
		if (self.symbol==other.symbol and self.date==other.date and self.timeSpan==other.timeSpan and self.timeUnit==other.timeUnit):
			return True
		else:
			return False

	def __lt__(self,other):
		if self.symbol != other.symbol:
			return (self.symbol < other.symbol)
		elif self.date < other.date:
			return True
		elif self.date == other.date:
			if self.getWeeks() < other.getWeeks():
				return True
		else:
			return False

	def __ne__(self,other):
		if self == other:
			return False
		else:
			return True

	def __gt__(self,other):
		if self.symbol!=other.symbol:
			return (self.symbol > other.symbol)
		elif self.date > other.date:
			return True
		elif self.date == other.date:
			if self.getWeeks() > other.getWeeks():
				return True
		else:
			return False

	def __ge__(self,other):
		if self > other or self == other:
			return True
		else:
			return False

	def __le__(self,other):
		if self < other or self == other:
			return False
		else:
			return True

	def __cmp__(self,other):
		if self == other:
			return 0
		elif self > other:
			return 1
		else:
			return -1
