from .AssociationModel import AssociationModel

class FieldValueModel(AssociationModel):

    def __init__(self, fields, row):
        self.field = fields
        self.row = row

    def getValue(self, field):
        return self.row[self.getField(field)]

    def getField(self, field):
        for index, f in enumerate(self.field):
            if (f == field):
                return index
        return None
