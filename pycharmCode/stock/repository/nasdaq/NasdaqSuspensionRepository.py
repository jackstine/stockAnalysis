from stock.streams.models import Model

class NasdaqSuspensionRepository:
    
    def __init__(self):
        pass

    def select(self, DB):
        model = Model("NasdaqIssuedSuspension")
        DB.select(model).execute()
        return model
