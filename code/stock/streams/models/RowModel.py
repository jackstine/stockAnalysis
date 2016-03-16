class RowModel:
    def __init__(self, data):
        self.data = data

    def getKey(self, index):
        return self.data[index]
