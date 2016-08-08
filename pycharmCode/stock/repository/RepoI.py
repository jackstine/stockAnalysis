from pycharmCode.stock.streams.models import Model, InsertModel
from pycharmCode.stock.streams.models.ModelAlgorithms import getPrimaryKeys, getDifference, getExisting
from pycharmCode.stock.streams.mysql import Ops
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
        self.querySelectAllIn(model, listIn, primaryKey).execute()
        return model

    def selectMax(self, field):
        model = Model(self.table)
        self.querySelectMax(model, field).execute()
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

    #given a list of entries, and the fields that we want to update,  look in the DB for the given entries
    #that match the primaryKey.  if those entries primary Keys are in the DB, then update those entires in
    # the datebase.Given entries, find the ones that match the database, then update those entires in the DB
    def _update(self, entries, fields, primaryKey):
        #NOTE all entries must be of InsertModel
        primaryKeysFromEntries = getPrimaryKeys(entries, primaryKey)
        dbList = self.selectAllIn(primaryKeysFromEntries, primaryKey)
        getExistingList = getExisting(dbList, entries, [primaryKey])
        differenceFields = fields + [primaryKey]    #get the list of fields that are going to be different
        modelsToUpdate = getDifference(dbList, getExistingList, differenceFields)
        self.update(modelsToUpdate, fields, primaryKey)

    #Given the entries and the Primary Keys of those entries, insert those entries that do not exist in the
    #database at all
    def _insert(self, entries, primaryKey):
        primaryKeys = getPrimaryKeys(entries, primaryKey)
        existingList = self.selectAllIn(primaryKeys,primaryKey)
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

    def getInsertModel(self):
        model = InsertModel(self.table)
        return model