from acunetix.acunetix import Acunetix

# get result
scan = Acunetix.get_scan_by_id('6bbad330-f2b2-469c-a217-1305bb41f37d')
if scan:
    results = Acunetix.get_results_of_scan(scan)
    print(results[0].id)

# get vulns of result
result = results[0]
vulns = Acunetix.get_vulns_of_result(result)

# detail vuln
print(vulns[0].detail())