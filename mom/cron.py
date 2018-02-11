from hostinfo import HostInfo
from requester import Requester


class Cron:
    def __init__(self):
        self._r = Requester()

    def execute(self):
        info = HostInfo().get_info()
        self._r.send_data_to_master(info)
