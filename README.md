# acunetix-sdk

## Model:

### Target:
```
class Target:
   target_id = targer-id
   address = address-of-target
   continuous_mode = false
   criticality = 10
   description = ""
   last_scan = <Class Scan>
   manual_intervention = null
 
   type = null,
   verification = null
```
### ScanProfile:
```
class ScanProfile:
  id = id
  name = "aaa"
  custom = True
  checks = [
    "name-of-check-1",
  ]
```
### Scan:
```
class Scan:
  scan_id = scan-id
  incremental = False
  
  max_scan_time = 0
  next_run = null
  
  current_session = <class Session>
  
  profile = <class ScanProfile>
  report = <class Report>
  
  target = <class Rarget>
  
  schedule = <class Schedule>
  
  result = [<class result>]
  
```
### Session:
```
class ScanSession:
    scan_session_id = scan-session-id
    event_level = 1
    progress = 0
    severity_counts = {
       "high": integer-number
       "info": integer-number
       "low": integer-number
       "medium": integer-number
    }
    start_date = start-date,
    status = processing
    threat = null
   
```
### Result:
```
class Result:
  result_id = result-id
  scan = <class Scan>
  start_date  =start-date
  end_date = end-date
  
  status = completed
  
  vulns = [<class Vulnerability>]
```

### Vulnerability
```
class Vulnerability:
  vuln_id = "2642100361078245058"
  affects_detail = "<empty>"
  affects_url = https://thihsattt.vn/"
  confidence = 80
  criticality = 10
  last_seen = null
  loc_id = 2
  severity = 2
  status = open
  target = <class Target>
  
```

### VulnDescription
```
class VulnDescription:
  vt_id = fa48a4-bd02-b3eb-1219-3d1f1f8a5143"
  vt_name = "TLS 1.0 enabled"
  cvss2 = "AV:N/AC:M/Au:N/C:P/I:N/A:N"
  cvss3 = "CVSS:3.0/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N"
  cvss_score = 3.1
  description = ""
  details = ""
  highlights = []
  impact = ""
  long_description = ""
  recommendation = ""
  references = []
  request = ""
  response_info = false
  source = "/Scripts/PerServer/SSL_Audit.script"
  tags = [
    "configuration",
    "CWE-16"
  ]
  target = <class Target>
  vuln = <class Vulnerability>
```

