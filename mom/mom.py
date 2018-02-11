import requests, sys
from consts import Consts
from settings import _Settings
from cron import Cron
import json


class Mom:
    def __init__(self):
        self._settings = _Settings()
        if len(sys.argv) == 2:
            self._register()
            sys.exit()
        else:
            cron = Cron()
            cron.execute()

    def _register(self):
        registration_key = sys.argv[1]
        r = requests.get(Consts.MAIN_SERVER_API_URL + "register?key=" + registration_key)
        if r.status_code is not 200:
            raise Exception('Error during first initialisation. API Error code: ' + str(r.status_code))
        api_key = r.text.strip()
        self._settings.set(key=api_key)
