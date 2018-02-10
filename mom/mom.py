import requests, sys
from consts import Consts
from settings import _Settings


class Mom:

    def __init__(self):
        if len(sys.argv) == 2:
            Mom.register()
            sys.exit()
        self._settings = _Settings()

    @staticmethod
    def register():
        try:
            s = _Settings()
        except:
            pass
        registration_key = sys.argv[1]
        r = requests.get(Consts.MAIN_SERVER_API_URL + "register?key=" + registration_key)
        if r.status_code is not 200:
            raise Exception('Error during first initialisation. API Error code: '+str(r.status_code))
        api_key = r.text.strip()
        s.set(key=api_key)
