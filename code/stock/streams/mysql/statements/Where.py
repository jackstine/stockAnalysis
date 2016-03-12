from .Condition import condition
from .MysqlStatement import MysqlStatement
from .GroupBy import GroupBy
from .And import And
import string

class Where(MysqlStatement):

    def __init__(self, mysql, model):
        MysqlStatement.__init__(self, mysql, model)
        self.mysql = mysql
        self.model = model

    def where(self, field, operator, comparator, statement = ""):
        self.query = condition(field, operator, comparator, statement, " WHERE ")
        if (statement == ""):
            return self

    def groupBy(self, fields, desc = False):
        groupBy = GroupBy(self.mysql, self.model)
        groupBy.groupBy(fields, self.query, desc)
        return groupBy

    def AND(self, field, operator, comparator):
        a = And(self.mysql, self.model)
        a.AND(field, operator, comparator, self.query)
        return a
