
class TableDescription:
    FIELD = 0
    TYPE = 1
    NULL = 2
    KEY = 3
    DEFAULT = 4
    EXTRA = 5
    fields = {"Field":FIELD, "Type":TYPE, "Null":NULL, "Key":KEY, "Default":DEFAULT, "Extra":EXTRA}
    PRIMARY_KEY = "PRI"
    MULTI_KEY = "MUL"
    ds = []

    def __init__(self, description):
        for d in description:
            from .Description import Description
            self.ds.append(Description(d,self.fields))

    def getFields(self):
        return self.fields

    def getPrimaryKeys(self):
        return self.getQueriedValues("Key", self.PRIMARY_KEY)

    def getMultiKeys(self):
        return self.getQueriedValues("Key", self.MULTI_KEY)
        
    def getQueriedValues(self, key, value):
        k = self.fields[key]
        primary = []
        for d in self.ds:
            if (d[key] == value):
                primary.append(d)
        return primary

    def sortFields(self, fields):
        sortedDescription = []
        for f in fields:
            for d in self.ds:
                if (f.getName() == d.getName().lower()):
                    sortedDescription.append(d)
                    break
        self.ds = sortedDescription

    def getFieldType(self, index):
        return self.getField(index)[TYPE]

    def getField(self, index):
        return self.ds[index]

    def isInteger(self, index):
        return self.ds[index].isInteger()

    def isDate(self, index):
        return self.ds[index].isDate()

    def isTimeStamp(self, index):
        return self.ds[index].isTimeStamp()

    def isDecimal(self, index):
        return self.ds[index].isTimeStamp()

    def isString(self, index):
        return self.ds[index].isString()
