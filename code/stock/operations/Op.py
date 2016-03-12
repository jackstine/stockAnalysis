class Op:
    def __init__(self, name = None):
        self.name = name

    def perform(self, table):
        for c in table.getCollections():
            c.perform(self)
            for r in c.getRows():
                r.append(self.performOp(r))

    def performOp(self, row):
        #This is a Template Method
        pass
