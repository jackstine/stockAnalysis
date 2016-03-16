class ModelBuilder:
    def __init__(self, models):
        self.models = models
        self.setModels()

    def setModels(self):
        firstModel = self.models[0]
        for model in self.models[1:]:
            firstModel.concate(model)
        self.model = firstModel

    def build(self, rows):
        for row in rows:
            self.model.addRow(row)
