from scrapy import Item, Field
class Quote(Item):
	bestBidAsk=Field()
	oneYearTarget=Field()
	highLow=Field()
	shareVolume=Field()
	didtyDayAvg=Field()
	previousClose=Field()
