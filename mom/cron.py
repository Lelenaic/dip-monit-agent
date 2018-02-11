from hostinfo import HostInfo
from mom import Mom


class Cron:
    def __init__(self):
        self._app = Mom()

    def execute(self):
        info = HostInfo().get_info()
        self._app.send_data_to_master(info)
