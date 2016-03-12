class Insert:

    def __init__(self, mysql):
        self.mysql = mysql;
        self.query = ''

    def insert(self, model):
        insertStatement = ''
        modelIsValid = model.table != None and model.hasFieldValues()
        if (modelIsValid):
            insertStatement = self._createInsertStatement(model)
        else:
            raise Exception("Insert needs Fields, or fields need Values to be inserted")
        self.query = insertStatement

    def _createInsertStatement(self, model):
        DELETE_COMMA = -2
        query = "INSERT INTO " + model.table + " SET "
        fields = model.getFields()
        values = model.getValues()
        for index, field in enumerate(model.getFields()):
            query += field + " = '" + values[index] + "', "
        return query[:DELETE_COMMA]

    def queue(self):
        self.mysql.queue(self.query)
