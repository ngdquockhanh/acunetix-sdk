
class Result:
    def __init__(self, id, start_date, scan, end_date=None, status=""):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.scan = scan
    