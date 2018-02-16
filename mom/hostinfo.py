import psutil


class HostInfo:
    def __init__(self):
        self._info = {}
        self._init_info()

    def _init_info(self):
        self._info['cpu'] = self.get_cpu_percent()
        self._info['uptime'] = psutil.boot_time()
        mem = self.get_memory()
        self._info['memory'] = {}
        self._info['memory']['total'] = mem.total
        self._info['memory']['used'] = mem.used
        self._info['disks'] = self.get_all_disks_info()
        self._info['process'] = self.get_process()
        self._info['network'] = self.get_network()

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

    @staticmethod
    def get_process():
        info = {}
        for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent']), key=lambda p: p.info['memory_percent'])[-10:]:
            info[p.info['name']] = p.info['memory_percent']
        return info

    @staticmethod
    def get_network():
        return {'download': (psutil.net_io_counters().bytes_recv)/1000, 'upload': (psutil.net_io_counters().bytes_sent)/1000}
