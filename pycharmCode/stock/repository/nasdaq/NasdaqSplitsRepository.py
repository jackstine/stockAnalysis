from stock.streams.models import Model

class NasdaqSplitsRepository:

    def __init__(self):
        pass

    def selectAll(self, db):
        model = Model("NasdaqSplits")
        db.select(model).execute()
        return model
