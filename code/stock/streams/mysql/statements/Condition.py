from ..Ops import Ops
from .MysqlStatement import MysqlStatement

def condition(field, operator, comparator, statement, text):
    if (isinstance(comparator, MysqlStatement)):
        return statement + text + field + " " + operator + " " + str(comparator)
    elif (operator == Ops.IN or operator == Ops.NOT_IN):
        whereStatement = (statement + text + field + " " + operator + " ('"
            + "', '".join(comparator) + "')")
        return whereStatement
    elif (operator == Ops.BETWEEN):
        whereStatement = (statement + text + field + " " + operator + " \"" + str(comparator[0]) + "\""
            + " AND \"" + str(comparator[1])) + "\""
        print whereStatement
        return whereStatement
    else:
        return statement + text + field + " " + operator + " '" + str(comparator) + "'"
