from abc import abstractmethod
from copy import copy

from classes.base import Base
from classes.statistics import Statistics, Statistic


class VmBase(Base):
    STATS_MODEL = Statistics([
            [ "memory.installed", "Total memory configured", "I", "G", "B" ],
            [ "memory.used", "Memory used (agent)", "I", "G", "B" ],
            [ "cpu.current.guest", "CPU used by guest", "D", "G", "P" ],
            [ "cpu.current.hypervisor", "CPU overhead", "D", "G", "P" ],
            [ "cpu.current.total", "Total CPU used", "D", "G", "P" ],
            [ "migration.progress", "Migration Progress", "D", "G", "P" ],
            [ "memory.buffered", "Memory buffered (agent)", "I", "G", "B" ],
            [ "memory.cached", "Memory cached (agent)", "I", "G", "B" ],
            [ "memory.free", "Memory free (agent)", "I", "G", "B" ],
        ])

    def __init__(self):
        super(Vm, self).__init__("vm")

        self.memory = 0
        self.cpu = Obj()
        self.cpu.sockets = 0
        self.cpu.cores = 0
        self.cpu.thread = 0
        self.created = None
        self.stopped = None
        self.disks = []
        self.nics = []
        self.stats = copy(self.STATS_MODEL)

    def get_statistics(self, guid = None):
        stat = self.stats.get(guid, None)
        if stat is None:
            raise NotFound()
        return stat

