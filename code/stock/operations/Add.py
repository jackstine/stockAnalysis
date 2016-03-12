from .Op import Op

class Add(Op):
    #NOTE field1 and field2 are the indexes of the fields
    def __init__(self, field1, field2, name=None):
        Op.__init__(self, name)
        self.field1 = field1
        self.field2 = field2

    def performOp(self, row):
        return self.field1.performOp(row) + self.field2.performOp(row)
