from .Table import Table

class DataPool:
    tables = dict()
    
    def __init__(self, stream):
        self.db = stream
        self.setTables()

    def setTables(self):
        for t in self.db.getTables():
            self.tables[t[0]] = Table(t[0], self.db)

    def getTableNames(self):
        return self.tables.keys()

    def getTable(self, tableName):
       return self.tables[tableName] 

    def __str__(self):
        string = ""
        for t in self.tables.iterkeys():
            string += t + "\n"
        return string
