from TableDescription import TableDescription

class Description:
    DATE_FIELD = "date"
    CHARACTER_FIELD = "character"
    VARCHAR_FIELD = "varchar"
    TIMESTAMP_FIELD = "timestamp"
    DECIMAL_FIELD = "decimal"
    INTEGER_FIELD = "int"   #TODO make sure that no other type has a "int" in it

    def __init__(self, d, fields):
        self.fields = fields
        self.d = d

    def __getitem__(self, name):
        return self.d[self.fields[name]]

    def isDate(self):
        return self.d[TableDescription.TYPE] == self.DATE_FIELD

    def isString(self):
        field = self.d[TableDescription.TYPE]
        return  self.VARCHAR_FIELD in field or self.CHARACTER_FIELD in field

    def isTimeStamp(self):
        return self.d[TableDescription.TYPE] == self.TIMESTAMP_FIELD

    def isDecimal(self):
        return  self.DECIMAL_FIELD in self.d[TableDescription.TYPE]

    def isInteger(self):
        v = self.d[TableDescription.TYPE]
        return self.INTEGER_FIELD in v

    def field(self):
        return self.d[self.fields["Field"]]

    def getName(self):
        return self.field()

    def __str__(self):
        return self.field()
