from Common.utility import Time
from pycharmCode.stock.repository import RepoI
from pycharmCode.stock.stockinfo.repos import IDSymbolRepo
from pycharmCode.stock.streams.models import Model


#because the Completes are similar, we will only need the name to be different
class CompletesRepo(RepoI):
    GOOGLE = "GoogleFinancialCompletes"
    NASDAQ = "NasdaqFinancialCompletes"
    YAHOO = "YahooFinancialCompletes"
    BLOOMBERG = "BloombergFinancialCompletes"

    def __init__(self, name, stream):
        self.table = name
        self.stream = stream
        RepoI.__init__(self, name, self.stream)
        self.reference = IDSymbolRepo(self.stream)

    def getCurrentFinancials(self,letter = None):
        if (letter == None):
            pass
        else:
            select = self.getCurrentFinancialsQuery(letter)
            select.execute()
            models = select.model
            return models


    def getCurrentFinancialsQuery(self,letter = None):
        completeModel = Model(self.table)
        select = self.reference.leftJoinQuery(completeModel, letter)
        completeModel2 = Model(self.table)
        completeModel2.addField("id")
        return select.AND("IDSymbol.id", self.stream.Ops.NOT_IN, self.stream.select(completeModel2).where(
            "DayExspectingQuarter", self.stream.Ops.GREATER_THAN, str(Time.now())))
        
