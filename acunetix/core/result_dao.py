from acunetix.model.result import Result
from acunetix.helper.api_call import APICall


class ResultDAO:
    def get_results_of_scan(scan):
        try:
            response = APICall.get('/scans/{}/results'.format(scan.id))
            raw_results = response['results']

            results = []

            for raw_result in raw_results:
                result_id = raw_result['result_id']
                start_date = raw_result['start_date']
                end_date = raw_result['end_date']
                status = raw_result['status']

                results.append(Result(id=result_id, start_date=start_date, scan=scan, end_date=end_date, status=status))

            return results
        except:
            return []
