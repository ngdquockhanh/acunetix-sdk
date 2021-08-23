from helper.api_call import APICall
from model.target import Target


class TargetDAO:
    def get_all_targets():
        try:
            response = APICall.get('/targets')
            raw_targets = response['targets']
            targets = []

            for target in raw_targets:
                id = target['target_id']
                address = target['address']
                description = target['description']
                criticality = target['criticality']
                continuous_mode = target['continuous_mode']
                manual_intervention = target['manual_intervention']
                type = target['type']
                verification = target['verification']
                status = target['last_scan_session_status']

                new_target = Target(id, address, description, criticality, continuous_mode,
                                    manual_intervention, type, verification, status)

                targets.append(new_target)

            return targets

        except:
            return None

    def get_target_by_id(id):
        try:
            target = APICall.get('/targets/{}'.format(id))
            id = target['target_id']
            address = target['address']
            description = target['description']
            criticality = target['criticality']
            continuous_mode = target['continuous_mode']
            manual_intervention = target['manual_intervention']
            type = target['type']
            verification = target['verification']

            new_target = Target(id, address, description, criticality,
                                continuous_mode, manual_intervention, type, verification)
            return new_target

        except:
            return None

    def create_target(url, description=""):
        data = {
            "targets": [
                {
                    "address": url,
                    "description": description
                }
            ],
            "groups": []
        }
        try:
            respose = APICall.post('/targets/add', data)
            target = respose['targets'][0]

            id = target['target_id']
            address = target['address']
            criticality = target['criticality']
            description = target['description']
            type = target['type']

            return Target(id, address, description, criticality, type=type)
        except:
            return None

    def create_targets(list_target):
        data = {
            "targets": list_target,
            "groups": []
        }
        try:
            respose = APICall.post('/targets/add', data)
            raw_targets = respose['targets']

            targets = []

            for target in raw_targets:
                id = target['target_id']
                address = target['address']
                criticality = target['criticality']
                description = target['description']
                type = target['type']

                targets.append(
                    Target(id, address, description, criticality, type=type))

            return targets

        except:
            return []

    def delete_target(ids):
        data = {
            "target_id_list": ids
        }
        return APICall.post_raw('/targets/delete', data)
