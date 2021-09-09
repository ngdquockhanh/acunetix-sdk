from acunetix.helper.api_call import APICall
from acunetix.model.target import Target
import re


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
            id = id.strip()
            id = id.lower()
            if len(id) > 255:
                return None
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
        if not re.fullmatch(r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$", url, re.IGNORECASE):
            return None

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
        r = re.compile(r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$", re.IGNORECASE)
        tmp_targets = []

        for i in list_target:
            url = str(i['address'])
            if r.match(url):
                tmp_targets.append(i)

        data = {
            "targets": tmp_targets,
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

    def delete_targets(ids):
        ids = [x for x in ids if len(x) <= 255]
        data = {
            "target_id_list": ids
        }
        return APICall.post_raw('/targets/delete', data)
