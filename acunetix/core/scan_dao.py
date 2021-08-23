import json
from model.result import Result
from helper.api_call import APICall
from config import PROFILES
from model.scan import Scan


class ScanDAO:
    def create_scan(target, profile_id=PROFILES['full_scan'], schedule={"disable": False, "start_date": None, "time_sensitive": False}):
        data = {
            "profile_id": profile_id,
            "incremental": False,
            "schedule": schedule,
            "target_id": target.id
        }
        try:
            res = APICall.post_raw('/scans', data)
            response = json.loads(res.text)

            scan_id = res.headers['Location'].split('/')[-1]
            incremental = response['incremental']
            max_scan_time = response['max_scan_time']

            new_scan = Scan(id=scan_id, profile=profile_id, incremental=incremental,
                            max_scan_time=max_scan_time, schedule=schedule, target=target)

            return new_scan
        except:
            return None

    def get_scan_by_id(scan_id):
        scan = APICall.get('/scans/{}'.format(scan_id))
        id = scan['scan_id']
        profile = scan['profile_id']
        incremental = scan['incremental']
        max_scan_time = scan['max_scan_time']
        next_run = scan['next_run']
        report = scan['report_template_id']
        schedule = scan['schedule']

        new_scan = Scan(id, profile, incremental=incremental,
                        max_scan_time=max_scan_time, next_run=next_run, report=report, schedule=schedule)

        return new_scan

    def stop_scan(scan):
        return APICall.post('/scans/{}/abort'.format(scan.id))

    def pause_scan(scan):
        return APICall.post('/scans/{}/pause'.format(scan.id))

    def resume_scan(scan):
        return APICall.post('/scans/{}/resume'.format(scan.id))

    def delete_scan(scan):
        return APICall.delete('/scans/{}'.format(scan.id))
