#returned by all Select statements

class Model:

    def __init__(self, table, data = None):
        self.table = table
        self.fields = []
        self.values = []
        self.fieldValues = []

    def getFields(self):
        return self.fields

    def getDictFields(self):
        dictOfFields = {}
        for index,field in enumerate(self.fields):
            dictOfFields[field.lower()] = index
        return dictOfFields

    def concate(self, model):
        fields = model.getFields()
        for f in fields:
            self.addField(model.table + "." + f)

    def getField(self, stringField):
        for index,f in enumerate(self.fields):
            print f
            if (stringField == f):
                return index
        return None

    def getValues(self):
        return self.values

    def addField(self, field):
        self.fields.append(field.lower())

    def getValue(self, field):
        for index, f in enumerate(self.fields):
            if (field.lower() == f):
                return self.values[index]

    def addFields(self, fields):
        for field in fields:
            self.fields.append(field.lower())

    def addFieldValue(self, field, value):
        if (value == None):
            self.values.append("NULL")
        self.fields.append(field.lower())
        self.values.append(value)

    def getRows(self):
        return self.fieldValues

    def getDictRows(self):
        rows = []
        for row in self.fieldValues:
            theD = dict()
            for rindex,r in enumerate(row):
                theD[self.fields[rindex].lower()] = r
            rows.append(theD)
        return rows

    def addFieldValues(self, fields, values):
        if (len(fields) == len(values)):
            for index, field in enumerate(fields):
                self.addFieldValue(field, values[index])
        else:
            raise Exception("the number of fields does not meet the number of values")

    def addRows(self, rows):
        for row in rows:
            self.addRow(row)

    def addRow(self, row):
        valid = len(row) == len(self.getFields())
        if (valid):
            self._addFieldValues()
            stringRow = []
            for r in row:
                stringRow.append(str(r))
            self.fieldValues[len(self.fieldValues) - 1] = stringRow
        else:
            raise Exception("the number of fields does not match the number of values in the row")

    def hasFieldValues(self):
        hasFields = len(self.fields) != 0
        hasValues = len(self.values) != 0
        if ( hasFields and hasValues):
            fieldsEqualsValues = len(self.fields) == len(self.values)
            if (fieldsEqualsValues):
            	return True
            else:
                return False
        else:
            return False

    def hasFields(self):
        return len(self.fields) > 0;

    def _addFieldValues(self):
        self.fieldValues.append([])

    def __str__(self):
        string = ""
        for row in self.fieldValues:
            for value in row:
                string += str(value)
            string += "\n"
        return string
