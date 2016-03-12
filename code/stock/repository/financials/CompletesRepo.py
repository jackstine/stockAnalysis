from .. import Repo
from ..nasdaq import NasdaqReferenceRepository
from ...models import Model
from ...utility import Time

#because the Completes are similar, we will only need the name to be different
class CompletesRepo(Repo):
    GOOGLE = "GoogleFinancialCompletes"
    NASDAQ = "NasdaqFinancialCompletes"
    YAHOO = "YahooFinancialCompletes"
    BLOOMBERG = "BloombergFinancialCompletes"

    def __init__(self, name):
        self.table = name
        Repo.__init__(self, name)
        self.reference = NasdaqReferenceRepository()

    def getCurrentFinancials(self, mysql, letter = None):
        if (letter == None):
            pass
        else:
            select = self.getCurrentFinancialsQuery(mysql, letter)
            select.execute()
            return select.model

    def getCurrentFinancialsQuery(self, mysql, letter = None):
        completeModel = Model(self.table)
        select = self.reference.leftJoinQuery(completeModel, letter, mysql)
        completeModel2 = Model(self.table)
        completeModel2.addField("symbol")
        return select.AND("NasdaqListingReference.symbol", mysql.Ops.NOT_IN, mysql.select(completeModel2).where(
            "DayExspectingQuarter", mysql.Ops.GREATER_THAN, str(Time.now())))
        
