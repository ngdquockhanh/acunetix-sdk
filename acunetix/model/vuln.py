from acunetix.model.vuln_des import VulnDesciption
from acunetix.helper.api_call import APICall


class Vulnerability:
    def __init__(self, id, name, affects_url, affects_detail, confidence, criticality, last_seen, severity, status, result):
        self.id = id
        self.name = name
        self.affects_url = affects_url
        self.affects_detail = affects_detail
        self.confidence = confidence
        self.criticality = criticality
        self.last_seen = last_seen
        self.severity = severity
        self.status = status
        self.result = result

    def detail(self):
        endpoint = '/scans/{}/results/{}/vulnerabilities/{}'.format(
            self.result.scan.id, self.result.id, self.id)
        response = APICall.get(endpoint)
        id = response['vt_id']
        name = response['vt_name']
        cvss2 = response['cvss2']
        cvss3 = response['cvss3']
        cvss_score = response['cvss_score']
        description = response['description']
        details = response['details']
        highlights = response['highlights']
        impact = response['impact']
        long_description = response['long_description']
        recommendation = response['recommendation']
        references = response['references']
        request = response['request']
        response_info = response['response_info']
        source = response['source']
        tags = response['tags']

        return VulnDesciption(id, name, cvss2, cvss3, cvss_score, description, details, highlights,
                              impact, long_description, recommendation, references, request, response_info, source, tags)
