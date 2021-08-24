from acunetix.config import *
import requests
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class APICall:
    __apibase = API_BASE
    __apikey = API_KEY
    __headers = {
        "X-Auth": __apikey,
        "content-type": "application/json",
    }

    def __json(data):
        try:
            return json.loads(data)
        except:
            None

    def __send_request(method='get', endpoint="", data=None):
        request_call = getattr(requests, method)
        url = str("{}{}".format(APICall.__apibase, endpoint if endpoint else "/"))
        try:
            response = request_call(
                url,
                headers = APICall.__headers,
                data = json.dumps(data),
                verify = False
            )
            return APICall.__json(response.text)
        except:
            return None

    def get_raw(endpoint=""):
        url = str("{}{}".format(APICall.__apibase, endpoint if endpoint else "/"))
        try:
            response = requests.get(url, headers=APICall.__headers, verify=False)
            return response
        except:
            return None

    def post_raw(endpoint, data={}):
        url = str("{}{}".format(APICall.__apibase, endpoint if endpoint else "/"))
        try:
            response = requests.post(url, headers=APICall.__headers, json=data, allow_redirects=False, verify=False)
            return response
        except:
            return None

    def delete_raw(endpoint, data={}):
        url = str("{}{}".format(APICall.__apibase, endpoint if endpoint else "/"))
        try:
            response = requests.delete(url, headers=APICall.__headers, json=data, allow_redirects=False, verify=False)
            return response
        except:
            return None

    def get(endpoint=""):
        return APICall.__send_request("get", endpoint)

    def post(endpoint, data={}):
        return APICall.__send_request("post", endpoint, data)

    def delete(endpoint, data={}):
        return APICall.__send_request("delete", endpoint, data)