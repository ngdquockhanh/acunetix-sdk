class ScanProfile:
    def __init__(self, id, name="", custom=False, checks=[]):
        self.id = id
        self.name = name
        self.custom = custom
        self.checks = checks