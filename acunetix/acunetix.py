from acunetix.helper.api_call import APICall
from acunetix.core.result_dao import ResultDAO
from acunetix.core.loc_dao import LocationDao
from acunetix.core.vuln_dao import VulnDAO
from acunetix.core.scan_dao import ScanDAO
from acunetix.core.target_dao import TargetDAO
from acunetix.config import PROFILES


class Acunetix:
    # target
    def create_target(url, description=""):
        return TargetDAO.create_target(url, description)

    def create_targets(list_target):
        return TargetDAO.create_targets(list_target)

    def get_target_by_id(id):
        return TargetDAO.get_target_by_id(id)

    def get_targets_by_ids(list_id):
        all_target = TargetDAO.get_all_targets()
        targets = [x for x in all_target if x.id in list_id]
        return targets

    def get_all_targets():
        return TargetDAO.get_all_targets()

    def delete_targets(list_id):
        return TargetDAO.delete_targets(list_id)

    # scan
    def create_scan_from_target(target, profile_id=PROFILES['full_scan'],
                                schedule={"disable": False, "start_date": None, "time_sensitive": False}):
        return ScanDAO.create_scan(target, profile_id, schedule)

    def get_all_scans():
        return ScanDAO.get_all_scans()

    def get_scan_by_id(id):
        return ScanDAO.get_scan_by_id(id)

    def get_scans_by_ids(list_id):
        all_scans = ScanDAO.get_all_scans()
        scans = [x for x in all_scans if x.id in list_id]
        return scans

    def pause_scan(scan):
        return ScanDAO.pause_scan(scan)

    def resume_scan(scan):
        return ScanDAO.resume_scan(scan)

    def stop_scan(scan):
        return ScanDAO.stop_scan(scan)

    def delete_scan(scan):
        return ScanDAO.delete_scan(scan)

    # result
    def get_results_of_scan(scan):
        return ResultDAO.get_results_of_scan(scan)

    # vulnerability
    def get_vulns_of_result(result):
        return VulnDAO.get_vulns_of_result(result)

    def get_result_statistic(result):
        return APICall.get('/scans/{}/results/{}/statistics'.format(result.scan.id, result.id))

    # location
    def get_root_location(result):
        return LocationDao.get_root_location(result)
