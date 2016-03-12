from .Condition import condition
from .MysqlStatement import MysqlStatement

class And(MysqlStatement):

    def __init__(self, mysql, model):
        MysqlStatement.__init__(self, mysql, model)
        self.model = model
        self.mysql = mysql

    def AND(self, field, operator, comparator, statement):
        self.query = condition(field, operator, comparator, statement, " AND ")

    def limit(self, number): 
        self.query += " LIMIT " + str(number) 
        return self 
