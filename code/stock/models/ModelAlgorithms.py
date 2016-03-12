from .FieldValueModel import FieldValueModel

def createDictFromModel(model, associationFields):
    fields = model.getFields()
    modelSet = dict()
    for r in model.getRows():
        m = FieldValueModel(fields, r)
        stringA = ""
        for f in associationFields:
            stringA += m.getValue(f)
        m.setAssociation(stringA)
        modelSet[stringA] = m
    return modelSet

def getPrimaryKeys(insertModels, primaryKey):
    #TODO add list primaryKeys
    keys = []
    for i in insertModels:
        keys.append(i.getValue(primaryKey))
    return keys

def getExisting(models, insertModels, fields):
    dif = getDifference(models, insertModels, fields)
    new = getStringInsertModels(insertModels, fields)
    for r in dif:
        new.discard(r)
    return new

def getDifference(models, insertModels, fields):
    oldStringModels = getStringModels(models, fields)
    new= getStringInsertModels(insertModels, fields)
    return new - oldStringModels

def getStringModels(models, fields):
    rows = models.getRows()
    properties = models.getDictFields()
    stringModels = set()
    for row in rows:
        string = ""
        for f in fields:
            string += row[properties[f.lower()]]
        stringModels.add(string)
    return stringModels

def getStringInsertModels(models, fields):
    stringModels = set()
    for m in models:
        string = ""
        for f in fields:
            string += m.getValue(f.lower())
        m.setAssociation(string)
        stringModels.add(m)
    return stringModels
