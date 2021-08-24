# acunetix-sdk

## Model:
```
class Target:
  id
  address
  description
  criticality
  continuous_mode
  manual_intervention
  type
  verification
  status
```
```
class Scan:
  id
  profile
  incremental
  max_scan_time
  next_run
  report
  schedule
  target
```
```
class Result:
  id
  start_date
  end_date
  status
  scan = <class Scan>
```
```
class Vulnerability:
  id
  name
  affects_url
  affects_detail
  confidence
  criticality
  last_seen
  severity
  status
  result: <class Result>
```
```
class VulnDescription:
  id
  name
  cvss2
  cvss3
  cvss_score
  description
  details
  highlights
  impact
  long_description
  recommendation
  references
  request
  response_info
  source
  tags
```
