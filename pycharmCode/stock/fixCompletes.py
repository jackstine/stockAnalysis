from pycharmCode.stock.streams.models import Model, InsertModel
from pycharmCode.stock.streams.mysql import DB


# table = "BloombergQuarterlyBalanceSheets"
# completesTable = "BloombergFinancialCompletes"
# db = DB(DB.Connections.STOCK)
# models = Model(table)
# db.select(models).execute()
# fields = models.getFields()
#
#
# idDates = dict()
#
# for m in models.getDictRows():
#     id = m["id"]
#     date = m["date"]
#     if (idDates.has_key(id)):
#         idDates[id].append(date)
#     else:
#         idDates[id] = []
#         idDates[id].append(date)
# for key,value in idDates.iteritems():
#     id = key
#     date = max(value)
#     insert = InsertModel(completesTable)
#     insert.insert("id", id)
#     insert.insert("tableName", table)
#     insert.insert("DayExspectingQuarter", date)
#     db.insert(insert).queue()
#
# db.commit()
#
# db.close()