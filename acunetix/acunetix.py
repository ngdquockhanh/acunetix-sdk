from helper.api_call import APICall
from core.loc_dao import LocationDao
from core.vuln_dao import VulnDAO
from core.scan_dao import ScanDAO
from core.target_dao import TargetDAO

class Acunetix:        
    def create_targets(list_target):
        return TargetDAO.create_targets(list_target)

    def create_new_scan(url):
        try:
            new_target = TargetDAO.create_target(url)
            new_scan = ScanDAO.create_scan(new_target)
            return new_scan
        except:
            return None

    def get_targets_by_id(list_id):
        all_target = TargetDAO.get_all_targets()
        targets = [x for x in all_target if x.id in list_id]
        return targets

    def get_vulns_of_result(result):
        return VulnDAO.get_vulns_of_result(result)
    
    def get_result_statistic(result):
        return APICall.get('/scans/{}/results/{}/statistics'.format(result.scan.id, result.id))

    def get_root_location(result):
        return LocationDao.get_root_location(result)