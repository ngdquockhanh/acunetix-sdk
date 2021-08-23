from model.localtion import Location
from helper.api_call import APICall

class LocationDao:
    def get_root_location(result):
        response = APICall.get('/scans/{}/results/{}/crawldata/0/children'.format(result.scan.id, result.id))
        raw_location = response['locations'][0]
        loc_id = raw_location['loc_id']
        loc_type = raw_location['loc_type']
        name = raw_location['name']
        parent = None
        path = raw_location['path']
        source = None
        tags = raw_location['tags']

        return Location(loc_id, loc_type, name, parent, path, source, tags, result)