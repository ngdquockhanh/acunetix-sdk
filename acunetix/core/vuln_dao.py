from acunetix.model.vuln import Vulnerability
from acunetix.helper.api_call import APICall


class VulnDAO:
    def get_vulns_of_result(result):
        try:
            response = APICall.get('/scans/{}/results/{}/vulnerabilities'.format(result.scan.id, result.id))
            raw_vulns = response['vulnerabilities']

            vulns = []

            for vuln in raw_vulns:
                id = vuln['vuln_id']
                name = vuln['vt_name']
                affects_url = vuln['affects_url']
                affects_detail = vuln['affects_detail']
                confidence = vuln['confidence']
                criticality = vuln['criticality']
                last_seen = vuln['last_seen']
                severity = vuln['severity']
                status = vuln['status']

                vulns.append(Vulnerability(id, name, affects_url, affects_detail, confidence, criticality, 
                last_seen, severity, status, result))
            
            return vulns
        
        except:
            return []