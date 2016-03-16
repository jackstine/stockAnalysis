from .Where import Where
from .And import And

class LeftJoin():

    def __init__(self, mysql):
        self.mysql = mysql
        self.query = ''
        self.listOfModels = []
        self.listOfAllFields = []

    def join(self, model1, model2, column):
        self.model = model1
        self.listOfModels.append(model1)
        self.listOfModels.append(model2)
        listOfModel1 = self._getModel(model1)
        listOfModel2 = self._getModel(model2)
        self.listOfAllFields = listOfModel1 + listOfModel2
        self.query = ("SELECT " + self._createTableQuery(listOfModel1, model1) 
            + ", " + self._createTableQuery(listOfModel2, model2) 
            + " FROM " + model1.table + " LEFT JOIN " + model2.table + " ON " 
            + self._getCol(model1, column) + " = " + self._getCol(model2, column))

    def where(self, field, operator, comparator):
        where = Where(self.mysql, self.model)
        where.where(field, operator, comparator, self.query)
        self.query = where.query
        return self

    def AND(self, field, operator, comparator):
        AND = And(self.mysql, self.model)
        AND.AND(field, operator, comparator, self.query)
        self.query = AND.query
        return self

    def execute(self):
        self.model = self.mysql.executeJoin(self.query, self.listOfAllFields, self.listOfModels)

    def _getModel(self, model):
    	valid = model.table != None
        if (valid):
            if (not model.hasFields()):
                return self._getAllFields(model)
            else:
                return self._getSelectedFields(model)

    def _getAllFields(self, model):
        fields = self.mysql.getFields(model.table)
        model.addFields(fields)
        return fields

    def _getSelectedFields(self, model):
        fields = model.getFields()
        return fields

    def _createTableQuery(self, fields, model):
       query = ""
       DELETE_COMMA = -1
       for field in fields:
            query += " " + self._getCol(model, field) + ","
       query = query[:DELETE_COMMA]
       return query

    def _getCol(self, model, col):
        return model.table + "." + col
     
