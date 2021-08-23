from helper.api_call import APICall
from core.loc_dao import LocationDao
from core.vuln_dao import VulnDAO
from core.result_dao import ResultDAO
from core.scan_dao import ScanDAO
from core.target_dao import TargetDAO

class Acunetix:        
    # tạo mới target
    def create_targets(list_target):
        return TargetDAO.create_targets(list_target)

    # tạo mới scan
    def create_new_scan(url):
        new_target = TargetDAO.create_target(url)
        new_scan = ScanDAO.create_scan(new_target)
        return new_scan

    # biểu diễn những target được scan
    def get_targets_by_id(list_id):
        all_target = TargetDAO.get_all_targets()
        targets = [x for x in all_target if x.id in list_id]
        return targets

    # biểu diễn danh sách các lỗ hổng từ kết quả scan
    def get_vulns_of_scan(scan, result_id=''):
        results = Acunetix.get_results_of_scan(scan)
        result = results[0]
        if result_id:
            result = [x for x in results if x.id == result_id][0]
        
        vulns = VulnDAO.get_vulns_of_result(result)
        return vulns
    
    # biểu thị trạng thái của quá trình scan theo thời gian
    def get_result_statistic(result):
        response = APICall.get('/scans/{}/results/{}/statistics'.format(result.scan.id, result.id))
        return response


    # biểu thị sitemap của website
    def get_root_location(result):
        return LocationDao.get_root_location(result)

scan = ScanDAO.get_scan_by_id('19b33e06-7a6f-4dc6-b2a2-567931125849')

result = ResultDAO.get_results_of_scan(scan)[0]

print(Acunetix.get_result_statistic(result))