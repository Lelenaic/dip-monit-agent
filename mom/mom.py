import requests, sys
from consts import Consts
from settings import _Settings


class Mom:

    def __init__(self):
        self._settings = _Settings()
        if len(sys.argv) == 2:
            self._register()
            sys.exit()

    def _register(self):
        registration_key = sys.argv[1]
        r = requests.get(Consts.MAIN_SERVER_API_URL + "register?key=" + registration_key)
        api_key = r.text.strip()
        self._settings.set(key=api_key)
