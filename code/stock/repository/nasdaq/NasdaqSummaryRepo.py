from stock.repository import RepoI
from stock.streams.mysql import DB
from Common.utility import Time
from stock.streams.models import Model

class NasdaqSummaryRepo(RepoI):
    def __init__(self):
        self.table = "NasdaqSummaryQuote"
        self.db = DB(DB.Connections.STOCK)
        RepoI.__init__(self, self.table, self.db, primary = "symbol")

    def selectQuarter(self):
        model = Model(self.table)
        quarter = Time.aQuarterAgo()
        otherDate = Time.addDays(quarter, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [quarter, otherDate]).execute()
        return model
        
    def selectMaxByDate(self):
        return RepoI.selectMaxByDate(self,"2015-10-02")#TODO       self.getMaxDate()) 

    def selectHalfAYear(self):
        model = Model(self.table)
        quarter = Time.halfAYearAgo()
        otherDate = Time.addDays(quarter, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [quarter, otherDate]).execute()
        return model

    def selectAYearAgo(self):
        model = Model(self.table)
        time = Time.aYearAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model

    def select3YearsAgo(self):
        model = Model(self.table)
        time = Time.threeYearsAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model

    def select5YearsAgo(self):
        model = Model(self.table)
        time = Time.fiveYearsAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model

    def select10YearsAgo(self):
        model = Model(self.table)
        time = Time.tenYearsAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model

    def select20YearsAgo(self):
        model = Model(self.table)
        time = Time.twentyYearsAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model

    def select30YearsAgo(self):
        model = Model(self.table)
        time = Time.thirtyYearsAgo()
        otherTime = Time.addDays(time, 5)
        self.db.select(model).where("date", self.db.Ops.BETWEEN, [time, otherTime]).execute()
        return model
