# acunetix-sdk

## Core:
### Class Acunetix:
- **create_target(url, description="")**  
  - tạo 1 target 
  - input: url, có thể có description hoặc không
  - output: đối tượng `Target` | `None`
  ```python
    target = Acunetix.create_target('http://google.com')
    # target =  <class Target>
  ```

- **create_targets(list_target)**
  - tạo nhiều target  
  - input: danh sách target `list_target`
  - output: danh sách các đối tượng `Target` | `[]`
  ```python
    list_target = [{"address": 'http://google.com',"description": "ndqk"}, {"address": 'http://google.com',"description": "ndqk2"}]
    targets = Acunetix.create_targets(list_target)
    # targets = [<class Target>, <class Target>]
  ```

- **get_target_by_id(target_id)** 
  - lấy 1 target theo id. 
  - input: `target_id`
  - ouput: đối tượng `Target` | `None`
  ```python
    target = Acunetix.get_target_by_id('abc')
    # target = <class Target>
  ```

- **get_targets_by_ids(list_id)**
  - lấy danh sách target theo danh sách id
  - input: danh sách id `list_id`
  - output: danh sách đối tượng `Target` | `[]`
  ```python
    targets = Acunetix.get_targets_by_ids(['abc', 'def'])
    # targets = [<class Target>, <class Target>]
  ```

- **get_all_targets()**
  - lấy danh sách tất cả các target có trong cơ sở dữ liệu của acunetix.
  - input: 
  - output: danh sách đối tượng `Target` | `[]`
  ```python
    targets = Acunetix.get_all_targets(['abc', 'def'])
    # targets = [<class Target>, <class Target>]
  ```

- **delete_targets(list_id)**
  - xóa các target nằm trong danh sách id.
  - input: danh sách id `list_id`
  - output: đối tượng `Response`
  ```
    Acunetix.delete_targets(['abc', 'def'])
  ```

- **create_scan_from_target(target, profile_id=,schedule=)**
  - tạo scan từ target đã tạo trước. 
  - input: đối tượng `Target`, `profile_id` và `schedule` (`profile_id`, `schedule` có thể có hoặc không)
  - output: đối tượng `Scan` | `None`
  ```python
    target = Acunetix.create_target('http://google.com')
    new_scan = Acunetix.create_scan_from_target(target)
    ## new_scan = <class Scan>
  ```

- **get_all_scans()**
  - lấy tất cả các scans có trong cơ sở dữ liệu Acunetix. 
  - input: 
  - output: danh sách đối tượng `Scan` | `[]`
  ```python
    all_scan = Acunetix.get_all_scans()
    # all_scan = [<class Scan>, ...]
  ```
  
- **get_scan_by_id(id)**
  - lấy scan theo id cho trước. 
  - input: id của scan
  - output: đối tượng `Scan` | `None`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    # scan = <class Scan>
  ```
   
- **get_scans_by_ids(list_id)**
  - lấy danh sách scan theo danh sách id cho trước. 
  - input: danh sách scan id
  - output: danh sách đối tượng `Scan` | `[]` 
  ```python
    scans = Acunetix.get_scans_by_ids(['abc', 'def'])
  ```

- **pause_scan(scan)**
  - tạm dừng 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    Acunetix.pause_scan(scan)
  ```
  
- **resume_scan(scan)**
  - khởi động lại 1 scan đang tạm dừng. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    Acunetix.pause_scan(scan)
    Acunetix.resume_scan(scan)
  ```
  
- **stop_scan(scan)**
  - kết thúc 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    Acunetix.stop_scan(scan)
  ```
  
- **delete_scan(scan)**
  - xóa 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    Acunetix.delete_scan(scan)
  ```

-   **get_results_of_scan(scan)**
  - lấy danh sách các reulst của 1 scan
  - input: đối tượng `Scan` 
  - output: danh sách các đối tượng `Result` |`[]`
  ```python
    scan = Acunetix.get_scan_by_id('abc')
    results = Acunetix.get_results_of_scan(scan)
  ```

- **get_vulns_of_result(result)**
  - lấy danh sách các lỗ hổng của 1 kết quả scan
  - input: đối tượng `Result`
  - output: danh sách các đối tượng `Vulnerability` | []
  ```python
     scan = Acunetix.get_scan_by_id('abc')
     results = Acunetix.get_results_of_scan(scan)
     result = results[0]
     vulns = Acunetix.get_vulns_of_result(result)
  ```
 
- **get_root_location(result)**
  - lấy thư mục gốc của trang web được scan
  - input: đối tượng `Result`
  - output: đối tượng `Location` | `None`
  ```python
     scan = Acunetix.get_scan_by_id('abc')
     results = Acunetix.get_results_of_scan(scan)
     result = results[0]
     root = Acunetix.get_root_location(result)
  ```

### class Location
- **childrens(self)**
  - lấy tất cả các thư mục con của chính thư mục này
  - input:
  - output: danh sách các đối tượng `Location` | []
  ```python
    root = Acunetix.get_root_location(result)
    root_childrens = root.children()
  ```

### class Vulnerability
- **detail(self)**
  - lấy chi tiết thông tin về lỗ hổng này
  - input:
  - output: đối tượng VulnDescription | None 
  ```python
    vulns = Acunetix.get_vulns_of_result(result)
    vuln = vulns[0]
    detail = vuln.detail()
  ```

## Model:
<p align="center">
  <img src="https://user-images.githubusercontent.com/87865134/130556809-52f38cb3-5d8c-4ac9-8ea9-09686dc861b4.jpg" />
</p>

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
```
class Location:
  loc_id
  loc_type
  name
  parent = <class Location>
  path
  source
  tags
  result = <class Result>
```

