class Collection:
    def __init__(self, table, rows):
        self.table = table 
        self.rows = rows

    def setModel(self, factory):
        for r in self.rows:
            self.r.setModel(factory(r))
        
    def getFields(self):
        return self.table.getFields()

    def getRows(self):
        return self.rows

    def getColumn(self, index):
        column = []
        for r in self.getRows():
            column.add(r[index])
        return column

    def perform(self, op):
        for r in self.getRows():
            r.append(op.performOp(r))

    #I do not think that this works
    def sort(self, key):
        self.rows = sorted(self.rows, key = lambda r: r.getKey(key))

    #DEP:  this was used to make the collection a Dynamic entity.
    #We got rid of this because it prevented us from defining a Model
    #The data Representation that Django takes is 
    #no doubt easy to understand than this method
    def setRef(self, reference, name):
        for r in self.rows:
            setattr(r,name,r.get(reference))

    def compileRows(self, compiler):
        for r in self.rows:
            compiler.perform(r)

    def __str__(self):
        return str(self.rows)
