class FinancialCompiler:
    def __init__(self):
        pass

    def perform(self, obj):
        self.setFreeCashFlow(obj)
        self.setNetProfitMargin(obj)
        self.setRORonSales(obj)
        self.setWorkingCapital(obj)
        self.setCurrentRatio(obj)
        self.setOperatingIncomePercent(obj)
        self.setAverageDailySales(obj)
        self.setQuickRatio(obj)
        self.setGrossProfitPercentage(obj)
        self.setProfitMargin(obj)
        self.setTimesInterestEarned(obj)
        self.setLeverageRatio(obj)
        self.setDebtRatio(obj)        

    def setDebtRatio(self, obj):
        d = obj.totalDebt / obj.totalAssets
        setattr(obj,"debtRatio",d)

    def setLeverageRatio(self, obj):
        l = obj.totalAssets / obj.totalEquity
        setattr(obj,"leverageRatio", l)

    def setTimesInterestEarned(self, obj):
        t = obj.cashFromOperatingActivities / obj.interestPaid
        setattr(obj,"timesInterestEarned", t)

    def setProfitMargin(self, obj):
        p = obj.netIncome / obj.revenue
        setattr(obj,"profitMargin", p)

    def setGrossProfitPercentage(self,obj):
        g = obj.grossProfit / obj.revenue
        setattr(obj,"grossProfitPercentage", g)

    def setQuickRatio(self, obj):
        q = (obj.cashEquivalents + obj.shortTermInvestments + obj.totalReceivable)  / obj.totalLiabilities
        setattr(obj,"quickRatio", q)

    def setAverageDailySales(self, obj):
        d = obj.revenue / 365
        setattr(obj,"averageDailySales", d)

    def setOperatingIncomePercent(self, obj):
        o = obj.operatingIncome / obj.revenue
        setattr(obj,"operatingIncomePercent", o)

    def setCurrentRatio(self, obj):
        c = obj.totalCurrentAssets / obj.totalLiabilities
        setattr(obj,"currentRatio", c)

    def setWorkingCapital(self, obj):
        w = obj.totalCurrentAssets - obj.totalCurrentLiabilities
        setattr(obj,"workingCapital", w)

    def setRORonSales(self,obj):
        r = (obj.netIncome - obj.preferredDividends) / obj.revenue
        setattr(obj,"RORonSales",r)

    def setNetProfitMargin(self,obj):
        m = obj.netIncome / obj.revenue
        setattr(obj,"netProfitMargin", m)

    def setFreeCashFlow(self, obj):
        f = obj.cashFromOperatingActivities - obj.cashFromInvestingActivities
        setattr(obj,"freeCashFlow", f)
