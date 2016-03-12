from scrapy import Field,Item
class CashItem(Item):
	Symbol = Field()
	Date = Field()
	TimeSpan = Field()
	TimeUnit = Field()
	Currency = Field()
	CurrencyUnit = Field()
	NetIncomeStartingLine = Field()
	DepreciationDepletion = Field()
	Amortization = Field()
	DeferredTaxes = Field()
	NonCashItems = Field()
	ChangesinWorkingCapital = Field()
	CashfromOperatingActivities = Field()
	CapitalExpenditures = Field()
	OtherInvestingCashFlowItemsTotal = Field()
	CashfromInvestingActivities = Field()
	FinancingCashFlowItems = Field()
	TotalCashDividendsPaid = Field()
	IssuanceRetirementofStockNet = Field()
	IssuanceRetirementofDebtNet = Field()
	CashfromFinancingActivities = Field()
	ForeignExchangeEffects = Field()
	NetChangeinCash = Field()
	CashInterestPaidSupplemental = Field()
	CashTaxesPaidSupplemental = Field()