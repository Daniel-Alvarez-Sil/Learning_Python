class EqualValuesException(Exception):
    def __init__(self, cMessage):
        self.message = cMessage