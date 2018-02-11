from consts import Consts
import json, requests
from settings import _Settings


class Requester:
    def __init__(self):
        self._url = Consts.MAIN_SERVER_API_URL
        self._settings = _Settings()

    def send_data_to_master(self, data):
        headers = {'Authorization': self._settings.get('key')}
        form_data = {'info': json.dumps(data, ensure_ascii=False)}
        requests.post(Consts.MAIN_SERVER_API_URL + "ping", form_data, headers=headers)
