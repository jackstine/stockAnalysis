from ..repository.table import TableRepo
from .Field import Field
from .TableDescription import TableDescription
from .sort import LogicalSort
from .Collection import Collection
from .Row import Row

class Table:

    def __init__(self, name, rows, fields, key, sortMethod, modelFactory):
        self.collections = []
        self.key = key
        self.fields = fields
        self.factory = modelFactory
        self._setCollections(rows)
        self.name = name
        self.sortCollections(sortMethod)

    def getRows(self):
        if (self.collections):
            pass
        else:
            self.getData()
            return self.getRows()

    def getCollections(self):
        return self.collections

    def getFields(self):
        return self.fields

    def getColumn(self, index):
        column = []
        for c in self.getCollections():
            column.extend(c.getColumn(index))
        return column

    def getFieldIndex(self, fieldName):
        fieldName = fieldName.lower()
        return f[fieldName]

    def perform(self, op):
        self._addField(op.name)
        op.perform(self)

    def sortCollections(self, key):
        index = self.fields[key]
        for c in self.collections:
            c.sort(index)

    #DEP: this is used to setRef
    def compileCollections(self, compiler):
        for c in self.collections:
            c.compileRows(compiler)

    #DEP: this is not wise
    def setRef(self, reference, name):
        index = self.fields.index(reference.lower())
        for c in self.collections:
            c.setRef(index, name)

    def _addField(self, field):
        self.fields.append(field)

    def _setCollections(self, rows):
        if (len(rows) == 0):
            raise Exception("The number od rows to the table is 0")
        fieldIndex = self.fields[self.key]
        first = 0
        sortedValue = rows[first][fieldIndex]
        rowsForCollection = []
        for r in rows:
            if (sortedValue != r[fieldIndex]):
                sortedValue = r[fieldIndex]
                c = Collection(self, rowsForCollection)
                rowsForCollection = []
                rowsForCollection.append(self.factory( r, self.fields))
                self.collections.append(c)
            else:
                rowsForCollection.append(self.factory( r, self.fields))
