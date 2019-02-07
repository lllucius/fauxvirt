from abc import abstractmethod
from copy import copy

from classes.base import Base
from classes.statistics import Statistics, Statistic

class HostBase(Base):
    STATS_MODEL = Statistics([
            [ "memory.total", "Total memory", "I", "G", "B" ],
            [ "memory.used", "Used memory", "I", "G", "B" ],
            [ "memory.free", "Free memory", "I", "G", "B" ],
            [ "memory.shared", "Shared memory", "I", "G", "B" ],
            [ "memory.buffers", "IO buffers", "I", "G", "B" ],
            [ "memory.cached", "OS caches", "I", "G", "B" ],
            [ "swap.total", "Total swap", "I", "G", "B" ],
            [ "swap.free", "Free swap", "I", "G", "B" ],
            [ "swap.used", "Used swap", "I", "G", "B" ],
            [ "swap.cached", "Swap also in memory", "I", "G", "B" ],
            [ "ksm.cpu.current", "KSM CPU usage", "D", "G", "P" ],
            [ "cpu.current.user", "User CPU usage", "D", "G", "P" ],
            [ "cpu.current.system", "System CPU usage", "D", "G", "P" ],
            [ "cpu.current.idle", "Idle CPU usage", "D", "G", "P" ],
            [ "cpu.load.avg.5m", "CPU 5 minute load average", "D", "G", "P" ],
            [ "boot.time", "Boot time of the machine", "I", "G", "N" ],
            [ "hugepages.1048576.free", "Amount of free huge pages of the given size", "I", "G", "N" ],
            [ "hugepages.2048.free", "Amount of free huge pages of the given size", "I", "G", "N" ],
        ])

    def __init__(self, init = None):
        super(HostBase, self).__init__("host")

        self.active = True
        self.address = None
        self.port = None
        self.memory = 0
        self.swap = 0
        self.cpus = 0
        self.cluster = None
        self.type = ""
        self.health = "ok"
        self.active_vms = 0
        self.migrating_vms = 0
        self.total_vms = 0
        self.fingerprint = ""
        self.stats = copy(self.STATS_MODEL)

        if init is not None:
            self.__dict__.update(init.items())

    def get_statistics(self, guid = None):
        stat = self.stats.get(guid, None)
        if stat is None:
            raise NotFound()
        return stat

