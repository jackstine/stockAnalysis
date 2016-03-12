from ..streams.mysql import DB
from ..models import Model, getDifference, ModelIter, InsertModel
from ..repository.financials import ConsolidatedRepo
from ..repository.nasdaq import NasdaqSummaryRepo

conTables = None

def consolidatePrices():
    global conTables
    db = DB(DB.Connections.STOCK)
    repo = ConsolidatedRepo()
    conTable = repo.table
    model = setLastPrice(conTable)
    setQuarterGain(model)
    setHalfYearGain(model)
    setYearGain(model)
    set3YearGain(model)
    set5YearGain(model)
    set10YearGain(model)
    set20YearGain(model)
    set30YearGain(model)
    insertAndUpdate(model, repo)

def setQuarterGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().selectQuarter())
    addValue(MI, "FirstQuarterGain", extendModel)

def setHalfYearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().selectHalfAYear())
    addValue(MI, "halfYearGain", extendModel)

def setYearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().selectAYearAgo())
    addValue(MI, "OneYearGain", extendModel)

def set3YearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().select3YearsAgo())
    addValue(MI, "ThreeYearGain", extendModel)

def set5YearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().select5YearsAgo())
    addValue(MI, "FiveYearGain", extendModel)

def set10YearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().select10YearsAgo())
    addValue(MI, "TenYearGain", extendModel)

def set20YearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().select20YearsAgo())
    addValue(MI, "TwentyYearGain", extendModel)

def set30YearGain(extendModel):
    MI = ModelIter(NasdaqSummaryRepo().select30YearsAgo())
    addValue(MI, "ThirtyYearGain", extendModel)

def addValue(MI, valueToAdd, extendModels):
    for m in extendModels:
        symbol = m.getValue("symbol")
        value = MI.getNext("symbol", symbol)
        if (value == None):
            m.insert(valueToAdd, None)
        else:
            quoteIndex = MI.getFieldIndex("quote")
            quote = float(value[quoteIndex])
            lastPrice = float(m.getValue("lastPrice"))
            value = (lastPrice - quote) / quote
            m.insert(valueToAdd, value)

def setLastPrice(conTable):
    model = NasdaqSummaryRepo().selectMaxByDate()
    print "***************DONE**DONE**DONE**DONE**DONE**DONE**DONE**"
    models = []
    quoteIndex = model.getDictFields()["quote"]
    symbolIndex = model.getDictFields()["symbol"]
    for m in model.getRows():
        IM = InsertModel(conTable)
        IM.insert("lastPrice", m[quoteIndex])
        IM.insert("symbol", m[symbolIndex])
        models.append(IM)
    return models

def insertAndUpdate(models, repo):
    db = DB(DB.Connections.STOCK)
    conModels = repo.selectAll()
    conSymbolIndex = conModels.getDictFields()["symbol"]
    conRows = conModels.getRows()
    conRowCount = 0
    for m in models:
        m.convertValuesToString()
        conSymbol = None
        if (conRowCount < len(conRows)):
            conSymbol = conRows[count][conSymbolIndex]
        modelSymbol = m.getValue("symbol")
        if (conSymbol == None or modelSymbol < conSymbol):
            db.insert(m).queue()
        elif (modelSymbol == conSymbol):
            db.update(m).where("symbol", db.Ops.EQUALS, conSymbol).queue()
    db.commit()
