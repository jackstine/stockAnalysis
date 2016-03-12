from ..models import Model
from ..streams.mysql import DB
from operator import itemgetter
from collections import Counter
import sets
import time

def cleanFinancial(table):
    primaries = ["symbol", "date"]
    model = Model(table)
    for p in primaries:
        model.addField(p)
    db = DB(DB.Connections.STOCK)
    query = "SELECT "
    for p in primaries:
        query += p + ","
    query = query[:len(query) - 1]
    query += " FROM " + table
    db.execute(query, model)
    rows = model.getRows()
    rows = sorted(rows, key =itemgetter(0,1) )
    collection = []
    collection.append([])
    addToCollection = rows[0][0]
    for r in rows:
        if (r[0] == addToCollection):
            collection[len(collection) - 1].append(r)
        else:
            collection.append([])
            addToCollection = r[0]
            collection[len(collection) - 1].append(r)
    for c in collection:
        symbol = c[0][0]
        count = Counter()
        theSet = sets.Set()
        for i in c:
            count[i[1]] += 1
            theSet.add(i[1])
        for s in theSet:
            if (count[s] > 1):
                # so now we need to delete count[s] - 1 intries
                amountToDelete = count[s] - 1
                model = Model(table)
                de = db.delete(model)
                wh = de.where("symbol", DB.Ops.EQUALS, symbol).AND("date", DB.Ops.EQUALS, s).limit(amountToDelete).queue()
    db.commit()
