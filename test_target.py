from acunetix.acunetix import Acunetix

description = ''
url = 'https://www.qaacharya@.in'

# target = Acunetix.create_target(url, description)
# print(target)

list_target = [
    {"address": 'http://google.com',"description": "ndqk"}, 
    {"address": 'https://www.qaacharya@.in',"description": "ndqk2"}]
# targets = Acunetix.create_targets(list_target)
# print(targets)

target_id = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1006adfc-aec1-43c7-9a1f-bdf859b8cfa0'
target_id = ''
# target = Acunetix.get_target_by_id(target_id)
# print(target)

list_id = ['1006adfc-aec1-43c7-9a1f-bdf859b8cfa0', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaS']
targets = Acunetix.get_targets_by_ids(list_id)
print(targets)

# all_target = Acunetix.get_all_targets()
# print(all_target)

list_id = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
print(Acunetix.delete_targets(list_id))