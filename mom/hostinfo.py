import psutil
from socket import gethostname


class HostInfo:
    def __init__(self):
        self._info = {}
        self._init_info()

    def _init_info(self):
        self._info['cpu'] = self.get_cpu_percent()
        mem = self.get_memory()
        self._info['memory'] = {}
        self._info['memory']['total'] = mem.total
        self._info['memory']['used'] = mem.used
        self._info['disks'] = self.get_all_disks_info()

    def get_info(self):
        return self._info

    @staticmethod
    def get_cpu_percent():
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_memory():
        return psutil.virtual_memory()

    @staticmethod
    def get_disk_usage(partition):
        return psutil.disk_usage(partition)

    @staticmethod
    def get_disk_list():
        return psutil.disk_partitions()

    @staticmethod
    def get_all_disks_info():
        info = {}
        disks = HostInfo.get_disk_list()
        for disk in disks:
            usage = HostInfo.get_disk_usage(disk.mountpoint)
            info[disk.device] = {}
            info[disk.device]['total'] = usage.total
            info[disk.device]['used'] = usage.used
        return info
