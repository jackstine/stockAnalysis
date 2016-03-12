class Field:

    def __init__(self, name, index):
        self._name = name
        self._index = index

    def getName(self):
        return self._name

    def getIndex(self):
        return self._index

    def __str__(self):
        return self._name
