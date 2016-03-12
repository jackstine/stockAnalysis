from .Add import Add
from .Sub import Sub
from .Div import Div
from .Mult import Mult
from .FieldOp import FieldOp

class SerializeOps:
    def __init__(self):
        pass

    def generateOp(self, string):
        #without ()
        # num + num / num - num * num
        fieldStack= []
        opStack = []
        for s in string.split(" "):
            if (isInt(s)):
                fieldStack.append(FieldOp(int(s)))
            elif (isOp(s)):
                opStack.append(getOp(s))
        field2 = None
        while(fieldStack != []):
            op = opStack.pop()
            field = fieldStack.pop()
            if (field2):
                field2 = op(field, field2)
            else:
                field2 = fieldStack.pop()
                field2 = op(field, field2)
        return field2

    def generateString(self, Op):
        pass


def isInt(s):
    """takes a string and sees if it is a Integer"""
    for c in s:
        v = ord(c)
        if (v in range(48,60)): #ASCII number range 0 to 9
            continue
        else:
            return False
    return True

def isOp(s):
    """takes a string to see if it is a op"""
    return getOp(s) != None

def getOp(s):
    ops = {"+":Add,"-":Sub,"/":Div,"*":Mult}
    if (s in ops):
        return ops[s]
    else:
        return None
