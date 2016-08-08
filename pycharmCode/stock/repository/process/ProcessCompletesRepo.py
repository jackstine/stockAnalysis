from pycharmCode.stock.repository import Repo
from pycharmCode.stock.streams.mysql import DB
from pycharmCode.stock.streams.mysql.connections import Connections


class ProcessCompletesRepo(Repo):
    def __init__(self, table):
        self.table = table
        Repo.__init__(self, self.table)

    def getLastDay(self):
        mysql = DB(Connections.STOCK)
        model = Repo.selectMax(self,"day", mysql)
        mysql.close()
        rows = model.getRows()
        if (len(rows) > 1):
            return model.getRows()[0][0]
        else:
            return None
