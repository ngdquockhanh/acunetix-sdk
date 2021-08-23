
class Scan:
    def __init__(self, id, profile, incremental=False, 
    max_scan_time=0, next_run=None, report=None, schedule=None, target=None, results=[]):
        self.id = id
        self.profile = profile
        self.inremental = incremental
        self.max_scan_time = max_scan_time
        self.next_run = next_run
        self.report = report
        self.schedule = schedule
        self.target = target
        self.results = results
    
   