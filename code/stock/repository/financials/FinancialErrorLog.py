from .. import Repo
from ...models import InsertModel
from ...utility import Filter

class FinancialErrorLog(Repo):
    def __init__(self):
        self.table = "FinancialErrorLog"
        Repo.__init__(self, self.table)
        self.f = Filter()

    def insert(self, mysql, message, symbol, table):
        m = InsertModel(self.table)
        m.insert("Message", self.f.filterForSQL(message))
        m.insert("Symbol", symbol)
        m.insert("TableName", table)
        mysql.insert(m).queue()
