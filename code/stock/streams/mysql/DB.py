import MySQLdb,operator
import string
from . import DESCRIBE
from .statements import Insert, Select, Delete, Update, Where, LeftJoin
from ...models import ModelBuilder, Model
from .Ops import Ops
from .connections import Connections

class DB:
    """
            All queries that select must be sorted in this handling object
            this Object is used to select, insert, delete, drop,....  all the above
            operations listed in the mysql handling
    """
    Ops = Ops()
    Connections = Connections()

    def __init__(self, connection):
        self.connection = connection
        self.model = None
        self.open()

    def open(self):
        self.con = MySQLdb.connect(host = self.connection.host, user = self.connection.user, 
            passwd = self.connection.passwd, db = self.connection.db)
        self.cur = self.con.cursor()

    def getFields(self, table):
        table = self.describe(table)
        return self._getOneFieldFromTable(table, DESCRIBE.FIELD)

    def getTypes(self, table):
        table = self.describe(table)
        return self._getOneFieldFromTable(table, DESCRIBE.TYPE)

    def describe(self, table):
        self.cur.execute("DESCRIBE " + table)
        return self.cur.fetchall()

    def getTables(self):
        self.cur.execute("SHOW TABLES")
        return self.cur.fetchall()

    def commitExecute(self, query):
        self.cur.execute(query)
        self.commit()

    def execute(self, query, model):
        self.cur.execute(query)
        model.addRows(self.cur)

    def executeQuery(self, query):
        self.cur.execute(query)
        return self.cur

    def commitFetch(self, query, *args):
        self.cur.execute(query, *args)
        return self.cur.fetchall()

    def executeJoin(self, query, fields, models):
        self.cur.execute(query)
        modelBuilder = ModelBuilder(models)
        modelBuilder.build(self.cur.fetchall())
        return modelBuilder.model

    def queue(self, query):
        self.cur.execute(query)

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()

    def insert(self, model):
        insert = Insert(self)
        insert.insert(model)
        return insert

    def select(self, model, MAX = None):
        self.model = model
        select = Select(self, model)
        select.select(MAX)
        return select

    def update(self, model):
        update = Update(self, model)
        update.update()
        return update

    def delete(self, model):
        delete = Delete(self)
        delete.delete(model)
        return delete

    def leftJoin(self, model1, model2, column):
        join = LeftJoin(self)
        join.join(model1, model2, column)
        return join

    def _getOneFieldFromTable(self, table, field):
        fields = []
        for row in table:
            fields.append(row[field])
        return fields

if __name__=="__main__":
    mysql=DB()
    f = {'Name': 'Zara', 'Age': 7}
    the = Model(f)
    print mysql.insert(the)
