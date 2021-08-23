from helper.api_call import APICall


class Location:
    def __init__(self, loc_id, loc_type, name, parent, path, source, tags, result):
        self.loc_id = loc_id
        self.loc_type = loc_type
        self.name = name
        self.parent = parent
        self.path = path
        self.source = source
        self.tags = tags
        self.result = result

    def childrens(self):
        response = APICall.get('/scans/{}/results/{}/crawldata/{}/children'.format(self.result.scan.id, self.result
                                                                                   .id, self.loc_id))
        raw_locations = response['locations']

        locations = []

        for location in raw_locations:
            loc_id = location['loc_id']
            loc_type = location['loc_type']
            name = location['name']
            parent = None
            path = location['path']
            source = None
            tags = location['tags']

            locations.append(Location(loc_id, loc_type, name, parent, path, source, tags, self.result))
            
        return locations
