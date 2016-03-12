from .. import DB
from ..connections import Connections

class Tables:
    def __init__(self):
        self.mysql = DB(Connections.STOCK)

    def hasNoTable(self, table):
        self.mysql.cur.execute("SHOW TABLES LIKE '" + table + "'")
        tables = self.mysql.cur.fetchall()
        return not len(tables) >= 1
