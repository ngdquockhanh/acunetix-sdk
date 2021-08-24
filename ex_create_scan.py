from acunetix.acunetix import Acunetix

list_target = [ {"address": 'http://google.com',"description": "ndqk"}]

new_targets = Acunetix.create_targets(list_target)

if new_targets:
    new_target = new_targets[0]
    new_scan = Acunetix.create_scan_from_target(new_target)
    print(new_scan)