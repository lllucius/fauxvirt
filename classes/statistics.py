from collections.abc import Mapping

from utils import make_guid

class Statistic(object):
    STAT_TYPES = {"I": "INTEGER", "D": "DECIMAL"}
    STAT_UNITS = {"N": "NONE", "P": "PERCENT", "B": "BYTES", "BS": "BYTES_PER_SECOND", "bs": "BITS_PER_SECOND", "S": "SECONDS", "CS": "COUNT_PER_SECOND"}
    STAT_KINDS = {"G": "GAUGE", "C": "COUNTER"}

    def __init__(self, statdef):
        super(Statistic, self).__init__()

        self.name = statdef[0]
        self.desc = statdef[1]
        self.type = self.STAT_TYPES[statdef[2]]
        self.kind = self.STAT_KINDS[statdef[3]]
        self.unit = self.STAT_UNITS[statdef[4]]
        self.value = 0
        self.id = make_guid("statistics", self.name)

class Statistics(Mapping):
    def __init__(self, statdefs):
        super(Statistics, self).__init__()

        self.stats = {}
        self.ids = {}
        for statdef in statdefs:
            stat = Statistic(statdef)
            self.stats[stat.name] = stat
            self.ids[stat.id] = stat.name

    def __getitem__(self, key):
        if key in self.ids:
            return self.stats[self.ids[key]]
        return self.stats[key]

    def __iter__(self):
        return iter(self.stats)

    def __len__(self):
        return len(self.stats)

    def __contains__(self, item):
        if item in self.ids:
            return True
        return item in self.stats

