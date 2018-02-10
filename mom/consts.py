import os


class Consts:
    MOM_HOME = os.path.dirname(os.path.abspath(__file__))[:-4]
    MAIN_SERVER_API_URL = "http://mom.dip.lenaic.me/api/"
    #MAIN_SERVER_API_URL = "http://localhost:5000/api/"
    MOM_SETTINGS_FILE = MOM_HOME + os.path.sep + "settings.yaml"
