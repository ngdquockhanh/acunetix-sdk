from acunetix.acunetix import Acunetix

target = Acunetix.get_target_by_id('13302f78-30f2-4eb8-9b5f-cee9f94287b2')
# print(target)

profile_id = '11111111-1111-1111-1111-111111111111'

# scan = Acunetix.create_scan_from_target(target, profile_id)
# print(scan.id)

# all_scan = Acunetix.get_all_scans()
# print(all_scan)

# scan_id = '16697137-8557-4d7f-89d0-6d9bd4743d5c'
# scan = Acunetix.get_scan_by_id(scan_id)
# print(scan.id)

# list_id = ['16697137-8557-4d7f-89d0-6d9bd4743d5c', '  ']
# scans = Acunetix.get_scans_by_ids(list_id)
# print(scans)

scan_id = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6bbad330-f2b2-469c-a217-1305bb41f37d'
scan = Acunetix.get_scan_by_id(scan_id)
print(scan)

# results = Acunetix.get_results_of_scan(scan)
# print(results)
# result = results[0]

# vuls = Acunetix.get_a