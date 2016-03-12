from ....models import Model
from .MysqlStatement import MysqlStatement

#NOTE it is assummed that the order of the fields are the order that they go into the Group By Statement
class GroupBy(MysqlStatement):

    def __init__(self, mysql, model):
        MysqlStatement.__init__(self, mysql, model)
        self.model = model

    def groupBy(self, fields, query, desc=False):
        self.query = query
        self._group(fields)
        if (desc):
            self.query += " DESC"

    def _group(self, fields):
        self.query += " Group By "
        for i,f in enumerate(fields):
            if (i == len(fields) - 1):
                self.query += f
            else:
                self.query += f + ", "
