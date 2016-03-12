from ..models import Model
from ..models.ModelAlgorithms import getPrimaryKeys, getDifference, getExisting
from ..streams.mysql import Ops
from datetime import datetime, timedelta


#NOTE this is DEPRECATED,  use REPOI
"""DEPRECATED use REPOI"""
class Repo:
    thirtyDays = timedelta(days = 30)

    def __init__(self, table, **kargs):
        self.keys = kargs
        self.table = table

    def selectAll(self, mysql):
        model = Model(self.table)
        mysql.select(model).execute()
        return model

    def selectAllIn(self, listIn, mysql, primaryKey):
        model = Model(self.table)
        self.querySelectAllIn(model, listIn, mysql, primaryKey).execute()
        return model

    def selectMax(self, field, mysql):
        model = Model(self.table)
        self.querySelectMax(model, field, mysql).execute()
        return model

    def update(self, updateModels, fields, primaryKey, mysql):
        for m in updateModels:
            mysql.update(m).where(primaryKey, mysql.Ops.EQUALS, m.getValue(primaryKey)).execute()

    def inserting(self, modelsToInsert, mysql):
        for m in modelsToInsert:
            mysql.insert(m).queue()

    def _update(self, entries, mysql, fields, primaryKey):
        #NOTE all entries must be of InsertModel
        primaryKeys = getPrimaryKeys(entries, primaryKey)
        listForUpdate = self.selectAllIn(primaryKeys, mysql, primaryKey)
        getExistingList = getExisting(listForUpdate, entries, [primaryKey]) 
        differenceFields = fields + [primaryKey]
        modelsToUpdate = getDifference(listForUpdate, getExistingList, differenceFields)
        self.update(modelsToUpdate, fields, primaryKey, mysql)

    def _insert(self, entries, mysql, primaryKey):
        primaryKeys = getPrimaryKeys(entries, primaryKey)
        existingList = self.selectAllIn(primaryKeys, mysql, primaryKey)
        modelsToInsert = getDifference(existingList, entries, [primaryKey])
        self.inserting(modelsToInsert, mysql)

    def selectWithIn30Days(self, mysql):
        model = Model(self.table)
        self.queryWithin30Days(mysql, model).execute()
        return model

    def queryWithin30Days(self, mysql, model):
        return mysql.select(model).where(self.keys['queryWithIn30Days'], Ops.GREATER_THAN, 
            str(datetime.now() - self.thirtyDays))

    def querySelectAllIn(self, model, listIn, mysql, primaryKey):
        return mysql.select(model).where(primaryKey, mysql.Ops.IN, listIn)

    def querySelectMax(self, model, field, mysql):
        return mysql.select(model, MAX = field)
