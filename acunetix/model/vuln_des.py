class VulnDesciption:
    def __init__(self, id, name, cvss2, cvss3, cvss_score, description, details, 
    highlights, impact, long_description, recommendation, references, request, response_info, source, tags):
        self.id = id
        self.name = name
        self.cvss2 = cvss2
        self.cvss3 = cvss3
        self.cvss_score = cvss_score
        self.description = description
        self.details = details
        self.highlights = highlights
        self.impact = impact
        self.long_description = long_description
        self.recommendation = recommendation
        self.references = references
        self.request = request
        self.response_info = response_info
        self.source = source
        self.tags = tags
    
    
