from pycharmCode.stock.streams.mysql.DB import DB
import datetime
_db = DB(DB.Connections.STOCK)

def getBoolean(keyValue):
    return _get(keyValue)[0][0] == "T"

def getDate(keyValue):
    return datetime.datetime.strptime(_get(keyValue)[0][0].split('.')[0], '%Y-%m-%d %H:%M:%S')



def insert(keyValue, Value):
    if not _has(keyValue):
        query = "INSERT INTO SystemConfigurations (keyValue, Value) VALUES ('%s', '%s')" % (keyValue, Value)
        _db.commitExecute(query)
    else:
        update(keyValue, Value)

def update(keyValue, Value):
    _db.commitExecute("UPDATE SystemConfigurations SET Value = '%s' WHERE keyValue ='%s'" % (Value, keyValue))

def _has(keyValue):
    try:
        value = _get(keyValue)[0]
        return True
    except:
        return False

def _get(keyValue):
    return _db.commitFetch("Select Value from SystemConfigurations WHERE KeyValue = '%s'" % keyValue)