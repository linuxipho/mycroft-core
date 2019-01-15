from mycroft.configuration import ConfigurationManager
import requests
from requests.auth import HTTPBasicAuth


class EkylibreApi:
    """Ekylibre API class"""

    def __init__(self):
        self.config_api = ConfigurationManager.get().get("ekylibre_api")
        self.url = self.config_api.get('url')
        self.version = self.config_api.get('version')
        self.user = self.config_api.get('user')
        self.tocken = self.config_api.get('tocken')
        self.endpoint = None
        self.credentials = HTTPBasicAuth(self.user, self.tocken)

    def get(self, endpoint, payload=None):
        try:
            url = self.url + "/" + self.version + "/" + endpoint
            r = requests.get(url, payload, auth=self.credentials)
            return r.json()

        except Exception:
            return 'Error'

    def post(self, endpoint, payload):
        try:
            url = self.url + "/" + self.version + "/" + endpoint
            r = requests.post(url, json=payload, auth=self.credentials)
            return r.json()

        except Exception:
            return 'Error'
