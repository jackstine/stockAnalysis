from sqlalchemy import create_engine
import pandas as pd

class _Con:
    con = None

    def __init__(self):
        if (self.con == None):
            self.set_up_engine()

    def set_up_engine(self):
        self.engine = create_engine("mysql://stock:stockaholic@127.0.0.1:3306/stock")
        self.con = self.engine.connect()

    def read_table(self,tableName, index = None):
        return pd.read_sql_table(tableName,self.con, index_col=index)

    def read_query(self,query, index = None):
        return pd.read_sql_query(query,self.con, index_col=index)

    def read_id(self,tableName, id, index = None):
        return pd.read_sql_query("SELECT * FROM " + str(tableName) + " WHERE id = " + str(id), self.con, index_col = index)

con = _Con()
