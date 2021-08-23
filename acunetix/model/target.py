class Target:
    def __init__(self, id, address, description="", criticality=10, continuous_mode=False, 
    manual_intervention=None, type=None,verification=None, status=None, scans=[]):
        self.id = id
        self.address = address
        self.description = description
        self.criticality = criticality
        self.continuous_mode = continuous_mode
        self.manual_intervention = manual_intervention
        self.type = type
        self.verification = verification
        self.scans = scans
        self.status = status
    