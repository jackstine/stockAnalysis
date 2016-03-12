from .Op import Op

class FieldOp(Op):

    def __init__(self, field):
        Op.__init__(self)
        self.field = field
        
    # Note might want to change field to the Field used by Tables, and not the Index
    def performOp(self, row):
        return row[self.field]
