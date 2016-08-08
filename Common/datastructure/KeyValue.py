class KeyValue:
    def __init__(self, value, key):
        self.value = value
        self.key = key

    def setKey(self, key):
        self.key = key

    def __hash__(self):
        return self.key.__hash__()

    def __cmp__(self, other):
        if (self.key < other):
            return -1
        elif (self.key > other):
            return 1
        else:
            return 0

    def __eq__(self, other):
        return self.key.__eq__(other)