from Op import Op

class Div(Op):

    def __init__(self, field1, field2, name = None):
        Op.__init__(self, name)
        self.field1 = field1
        self.field2 = field2

    def performOp(self, row):
        if self.field2.performOp(row) == 0:
            return 0
        else:
            return self.field1.performOp(row) / self.field2.performOp(row)
