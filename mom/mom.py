import requests, sys
from consts import Consts
from settings import _Settings


class Mom:

    def __init__(self):
        self._settings = _Settings()
        if len(sys.argv) == 2:
            self._register()
            sys.exit()

    def _send_data(self):
        requests.post()

    def _register(self):
        registration_key = sys.argv[1]
        self._settings.set(key=registration_key)
