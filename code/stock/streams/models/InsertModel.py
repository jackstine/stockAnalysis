from .AssociationModel import AssociationModel

class InsertModel(AssociationModel):

    def __init__(self, table):
        self.table = table;
        self.fieldValues = dict()
        self.association = ""

    def insertField(self, field):
        self.fieldValues[field.lower()] = None

    def insert(self, field, value):
        if (value == None):
            self.fieldValues[field.lower()] = "None"
        else:
            self.fieldValues[field.lower()] = value

    def remove(self, field):
        del self.fieldValues[field]

    def getFields(self):
        return self.fieldValues.viewkeys()

    def getValues(self):
        return list(self.fieldValues.viewvalues())

    def getValue(self, field):
        return self.fieldValues[field.lower()]

    def hasFieldValues(self):
        values = self.fieldValues.viewvalues() 
        for v in values:
            if (v == None):
                return False
        return True

    def convertValuesToString(self):
        for v in self.fieldValues:
            self.fieldValues[v] = str(self.fieldValues[v])

    def addRows(self, something):
        """This does nothing"""
        pass

    def __str__(self):
        return str(self.fieldValues)

