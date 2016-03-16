from .Where import Where

class Update:
    query = ''

    def __init__(self, mysql, model):
        self.model = model
        self.mysql = mysql

    def update(self):
        if (self.model.table != None):
            if (self.model.hasFieldValues()):
                self.query = self._updateFields(self.model)
            else:
                raise Exception("Update needs fields to update, and values as well")
        else:
            raise Exception("Update needs a table to update")

    def execute(self):
        self.mysql.execute(self.query)

    def where(self, field, operator, comparator):
        where = Where(self.mysql, self.model)
        where.where(field, operator, comparator, self.query)
        return where

    def _updateFields(self, model):
        DELETE_COMMA = -1
        query = "UPDATE " + model.table + " SET "
        for field in model.getFields():
            query += " " + field + " = '" + model.getValue(field) + "',"
        query = query[:DELETE_COMMA]
        return query
