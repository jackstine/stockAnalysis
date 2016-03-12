from ..models import Model
from ..models.ModelAlgorithms import getPrimaryKeys, getDifference, getExisting
from ..streams.mysql import Ops
from datetime import datetime, timedelta

class RepoI:
    thirtyDays = timedelta(days = 30)

    def __init__(self, table, db, **kargs):
        self.keys = kargs
        self.table = table
        self.db = db

    #Returns the enter table
    def selectAll(self):
        model = Model(self.table)
        self.db.select(model).execute()
        return model

    #returns the table with a Sorting Method
    def selectAllSort(self, sort):
        model = Model(self.table)
        self.db.select(model).groupBy(sort.groupBy , sort.desc).execute()
        return model

    #uses the bases of   SELECT * FROM DB WHERE primaryKey IN listin
    #selects all the rows with the primaryKey is equal to any value in the listin
    def selectAllIn(self, listIn, primaryKey):
        model = Model(self.table)
        self.querySelectAllIn(model, listIn, self.db, primaryKey).execute()
        return model

    def selectMax(self, field):
        model = Model(self.table)
        self.querySelectMax(model, field, self.db).execute()
        return model

    def getMaxDate(self):
        model = Model(self.table)
        model.addField("date")
        self.db.select(model, "date").execute()
        return model.getRows()[0]   #returns the max date

    def selectMaxByDate(self, date):
        model = Model(self.table)
        other = self.db.select(model).where("date", self.db.Ops.EQUALS, date).groupBy([self.keys["primary"]]).execute()
        return model

    def update(self, updateModels, fields, primaryKey):
        for m in updateModels:
            self.db.update(m).where(primaryKey, self.db.Ops.EQUALS, m.getValue(primaryKey)).execute()

    def inserting(self, modelsToInsert):
        for m in modelsToInsert:
            self.db.insert(m).queue()

    def insertSingle(self, model):
        self.db.insert(model).queue()

    def _update(self, entries, fields, primaryKey):
        #NOTE all entries must be of InsertModel
        primaryKeys = getPrimaryKeys(entries, primaryKey)
        listForUpdate = self.selectAllIn(primaryKeys, self.db, primaryKey)
        getExistingList = getExisting(listForUpdate, entries, [primaryKey]) 
        differenceFields = fields + [primaryKey]
        modelsToUpdate = getDifference(listForUpdate, getExistingList, differenceFields)
        self.update(modelsToUpdate, fields, primaryKey, self.db)

    def _insert(self, entries, primaryKey):
        primaryKeys = getPrimaryKeys(entries, primaryKey)
        existingList = self.selectAllIn(primaryKeys, self.db, primaryKey)
        modelsToInsert = getDifference(existingList, entries, [primaryKey])
        self.inserting(modelsToInsert)

    def selectWithIn30Days(self):
        model = Model(self.table)
        self.queryWithin30Days(model).execute()
        return model

    def queryWithin30Days(self, model):
        return self.db.select(model).where(self.keys['queryWithIn30Days'], Ops.GREATER_THAN, 
            str(datetime.now() - self.thirtyDays))

    def querySelectAllIn(self, model, listIn, primaryKey):
        return self.db.select(model).where(primaryKey, self.db.Ops.IN, listIn)

    def querySelectMax(self, model, field):
        return self.db.select(model, MAX = field)
