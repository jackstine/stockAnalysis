from stock.tables import DataPool
from stock.streams.mysql import DB
from stock.operations import Add, FieldOp, SerializeOps

dp = DataPool(DB(DB.Connections.STOCK))
table = dp.getTable("NasdaqAnnualIncomeStatements")
table.getRows()
fields = table.getFields()
incomeTaxIndex = table.getFieldIndex("incomeTax")
totalRev = table.getFieldIndex("totalRevenue")
#add = Add("Cost+Tax", FieldOp(incomeTaxIndex), FieldOp(totalRev))
stringOp = str(incomeTaxIndex) + " + " + str(totalRev)
add = SerializeOps().generateOp(stringOp)
table.perform(add)
col0 = table.getColumn(incomeTaxIndex)
col1 = table.getColumn(totalRev)
col2 = table.getColumn(len(fields))
i = 0
length = len(col0)
while(i < length):
    print str(col0[i]) + " + " + str(col1[i]) + " = " + str(col2[i])
    i += 1
