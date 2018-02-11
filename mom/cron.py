from hostinfo import HostInfo
from mom import Mom

info = HostInfo().get_info()
app = Mom()
app.send_data_to_master(info)
