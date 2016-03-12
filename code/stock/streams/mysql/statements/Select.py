from .Where import Where
from .GroupBy import GroupBy
from .MysqlStatement import MysqlStatement
from .LeftJoin import LeftJoin
from ....models import Model

class Select(MysqlStatement):

    def __init__(self, mysql, model):
        MysqlStatement.__init__(self, mysql, model)
        self.model = model
        self.query = ''

    def select(self, MAX = None):
        modelIsValid = self.model.table != None
        if (modelIsValid):
            if (self.model.hasFields()):
                self.query = self._selectSelectedFields(MAX)
            else:
                self.query = self._selectAllFields(MAX)
        else:
            raise Exception("Select must have a Table name")

    def where(self, field, operator, comparator):
        where = Where(self.mysql, self.model)
        where.where(field, operator, comparator, self.query)
        return where

    def groupBy(self, fields, desc = False):
        groupBy = GroupBy(self.mysql, self.model)
        groupBy.groupBy(fields, self.query, desc)
        return groupBy

    def _selectAllFields(self, MAX):
       fields = self.mysql.getFields(self.model.table)
       self.model.addFields(fields)
       return self._createSelectQuery(fields, self.model.table, MAX)

    def _selectSelectedFields(self, MAX = None):
        return self._createSelectQuery(self.model.getFields(), self.model.table, MAX)

    def _createSelectQuery(self, fields, table, MAX = None):
       query = "SELECT"
       DELETE_COMMA = -1
       for field in fields:
            if (MAX == field):
                query += " MAX(" + field + "),"
            else:
                query += " " +field + ","
       query = query[:DELETE_COMMA] + " FROM " + table
       return query
