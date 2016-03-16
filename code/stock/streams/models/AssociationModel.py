class AssociationModel:
    def __init__(self):
	pass

    def setAssociation(self, s):
        self.association = str(s)

    def __hash__(self):
        return self.association.__hash__()

    def __eq__(self, other):
        return self.association.__eq__(other)

    def __cmp__(self, other):
        if self.association > other:
            return -1
        elif self.association > other:
            return 1
        else:
            return 0
