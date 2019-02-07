import sys
import os
from datetime import datetime
import configparser

import untangle

from sdk import types as sdk
from sdk import services as svc
from sdk.enums import *
from utils import *

sdk.CurrentSubclassModule_ = sys.modules[__name__]

datacenters = {}
clusters = {}
disks = {}
files = {}
hosts = {}
networks = {}
storagedomains = {}
templates = {}
vms = {}

class Provider(object):
    def __init__(self):
        super().__init__()

        self.define_classes()

        global datacenters, clusters, disks, files, hosts
        global networks, storagedomains, templates, vms
        self.load_config()

    def define_classes(self):
        this = dir(sys.modules[__name__])
        d = untangle.parse("sdk/api.xsd")
        for e in d.xs_schema.get_elements("xs_complexType"):
            n = e["name"]
            if n not in this:
                self.define_class(n, getattr(sdk, n))

    def define_class(self, name, base):
        def __init__(self, *args, **kwargs):
            base.__init__(self, *args, **kwargs)
        globals()[name] = type(name, (base, ), {"__init__": __init__})

    def get_names(self, parent, val):
        names = getattr(parent, val, "")
        if len(names) > 0:
            names = names.replace(" ", "")
            if len(names) > 0:
                names = names.split(",")
        return names

    def load_config(self):
        class Obj(dict):
            def __init__(self, init):
                self.id = None
                self.name = None
                self.description = None

                self.__dict__.update(init.items())

            def __getitem__(self, key):
                return self.__dict__[key]

            def __iter__(self):
                return iter(self.__dict__)

            def __len__(self):
                return len(self.__dict__)

            def __contains__(self, item):
                return item in self.__dict__

        cfg = configparser.ConfigParser()
        cfg.read("providers/sim.cfg")

        defaults = Obj(cfg["DEFAULT"])

        print(self.get_names(defaults, "datacenters"))
        for dc in self.get_names(defaults, "datacenters"):
            dc = Obj(cfg[dc])
            names = self.get_names(dc, "clusters")

            dc.clusters = []
            dc.state = "up"

            datacenters[dc.id] = dc
            print("dc.id", dc.id)

            for c in names:
                c = Obj(cfg[c])
                names = self.get_names(c, "hosts")

                c.hosts = []
                c.datacenter = dc.id

                clusters[c.id] = c
                dc.clusters.append(c.id)

                for h in names:
                    h = Obj(cfg[h])

                    h.cluster = c.id
                    h.active = True
                    h.state = "up"
                    h.health = "ok"
                    h.memory = 32 * 1024 * 1024 * 1024
                    h.active_vms = 0
                    h.migrating_vms = 0
                    h.total_vms = 0
                    h.fingerprint = "SHA256:MzB/n+GFeAsH099eX6aLSUS6dG4vHYUFmnEXqeLOncw"

                    hosts[h.id] = h
                    c.hosts.append(h.id)

                t = Obj({})
                t.id = "00000000-0000-0000-0000-000000000000"
                t.name = "blank"
                t.desc = "Blank template"
                t.memory = 1073741824
                t.cpus = 1
                t.state = "ok"
                t.created = "2018-10-26T00:49:11.412-04:00"
                t.disks = []
                templates[t.id] = t

                names = self.get_names(c, "templates")
                c.templates = []

                for t in names:
                    t = Obj(cfg[t])

                    t.cluster = c.id
                    t.state = "ok"
                    t.created = "2018-10-26T00:49:11.412-04:00"

                    names = self.get_names(t, "disks")
                    t.disks = []

                    """
                    for d in names:
                        t.disks.append(cfg[d]["id"])
                    """
                    templates[t.id] = t

                names = self.get_names(c, "networks")
                c.networks = []

                for n in names:
                    c.networks.append(cfg[n]["id"])

            names = self.get_names(dc, "storagedomains")
            dc.storagedomains = []

            for sd in names:
                sd = Obj(cfg[sd])
                names = self.get_names(sd, "disks")

                sd.disks = []            
                sd.datacenter = dc.id
                sd.active = True
                sd.state = "ok"
                sd.size = 50 * 1024 * 1024 * 1024
                sd.used = 0
                sd.committed = 0

                storagedomains[sd.id] = sd
                dc.storagedomains.append(sd.id)

                for d in names:
                    d = Obj(cfg[d])

                    d.storagedomain = sd.id
                    d.state = "ok"

                    names = self.get_names(d, "template")
                    if len(names) > 0:
                        d.template = cfg[d.template]["id"]
                        templates[d.template].storagedomain = d.storagedomain
     
                    names = self.get_names(d, "vm")
                    if len(names) > 0:
                        d.vm = cfg[d.vm]["id"]
                   
                    disks[d.id] = d
                    sd.disks.append(d.id)

            names = self.get_names(dc, "networks")
            dc.networks = []

            for n in names:
                n = Obj(cfg[n])

                n.datacenter = dc.id
                n.active = True
                n.state = "operational"

                networks[n.id] = n
                dc.networks.append(n.id)

        print(datacenters)
        for dc in datacenters:
            dc = datacenters[dc]
            print("dc: ", dc.name, dc.id)

            for c in dc.clusters:
                c = clusters[c]
                print("  cluster: ", c.name, c.id)

                for h in c.hosts:
                    h = hosts[h]
                    print("    host: ", h.name, h.id)

                for t in templates:
                    t = templates[t]
                    print("    template: ", t.name, t.id)

                    for d in t.disks:
                        print("      disk: ", disks[d].name, disks[d].id)

                for n in c.networks:
                    print("    network: ", networks[n].name, networks[n].id)

            for sd in dc.storagedomains:
                sd = storagedomains[sd]
                print("  storagedomain: ", sd.name, sd.id)

                for d in sd.disks:
                    d = disks[d]
                    print("    disk: ", d.name, d.id)

            for n in dc.networks:
                n = networks[n]
                print("  network: ", n.name, n.id)

class ProviderType(object):
    STAT_TYPE = {"G": sdk.StatisticType.GAUGE,
                 "C": sdk.StatisticType.COUNTER}
    STAT_UNIT = {"N": sdk.StatisticUnit.NONE,
                 "P": sdk.StatisticUnit.PERCENT,
                 "B": sdk.StatisticUnit.BYTES,
                 "S": sdk.StatisticUnit.SECONDS,
                 "BS": sdk.StatisticUnit.BYTES_PER_SECOND,
                 "bs": sdk.StatisticUnit.BITS_PER_SECOND,
                 "CS": sdk.StatisticUnit.COUNT_PER_SECOND}
    STAT_KIND = {"I": sdk.ValueType.INTEGER,
                 "D": sdk.ValueType.DECIMAL,
                 "S": sdk.ValueType.STRING}

    def __init__(self, parent, guid = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent = parent

        if parent is not None:
            if hasattr(self, "id"):
                self.set_id(guid)

            if hasattr(self, "href"):
                self.set_href(svc.path_href(self))

        svc.add_links(self)
        svc.add_actions(self)

    def get_parent(self):
        return self.parent

    def make_stats(self, statdefs, values, **kwargs):
        stats = Statistics(self)

        for name in values:
            stat = Statistic(stats, svc.make_guid("statistics", name), **kwargs)
            stats.add_statistic(stat)

            sd = statdefs[name]
            stat.set_name(name)
            stat.set_description(sd[0])
            stat.set_type(self.STAT_TYPE[sd[2]])
            stat.set_unit(self.STAT_UNIT[sd[3]])
            stat.set_values(Values(self.STAT_KIND[sd[1]], [Value(values[name])]))

        return stats

# =============================================================================

class API(ProviderType, sdk.API):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        s = SpecialObjects()
        s.add_link(Link(href=svc.base_href("Templates", "00000000-0000-0000-0000-000000000000"), rel="templates/blank"))
        s.add_link(Link(href=svc.base_href("Tags", "00000000-0000-0000-0000-000000000000"), rel="tags/root"))
        self.set_special_objects(s)

        s = ApiSummary()
        s.set_hosts(Hosts(self, active=len(hosts), total=len(hosts)))
        s.set_users(Users(self, active=1, total=1))
        s.set_storage_domains(StorageDomains(self, active=len(storagedomains), total=len(storagedomains)))
        s.set_vms(VMs(self, active=len(vms), total=len(vms)))

        s = ProductInfo()
        s.set_name("zVirt API")
        s.set_version(Version(major="3", minor="6"))
        self.set_product_info(s)

        dt = self.gds_parse_datetime(svc.get_date())
        self.set_time(dt)

    @staticmethod
    def get(parent, guid):
        return API(parent, guid)

# =============================================================================

class DataCenters(ProviderType, sdk.DataCenters):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        coll = DataCenters(parent)

        for dc in datacenters:
            coll.add_data_center(DataCenter(coll, dc))

        return coll

class DataCenter(ProviderType, sdk.DataCenter):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        dc = datacenters[self.id]

        self.set_name(dc.name)
        self.set_description(dc.description)
        self.set_local(False)
        self.set_storage_format(StorageFormat.V3)
        self.set_status(Status(DataCenterStatus.UP))
        self.set_quota_mode(QuotaModeType.DISABLED)
        version = Version(major=3, minor=6)
        self.set_version(version)
        self.set_supported_versions(SupportedVersions([version]))

    @staticmethod
    def get(parent, guid):
        for dc in parent.get_data_center():
            if dc.id == guid:
                return dc

        return None

# =============================================================================

class Clusters(ProviderType, sdk.Clusters):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            pid = parent.get_id()

        coll = Clusters(parent)
        for c in clusters:
            if not pid or clusters[c].datacenter == pid:
                coll.add_cluster(Cluster(coll, c))

        return coll
        
class Cluster(ProviderType, sdk.Cluster):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        c = clusters[self.id]

        self.set_name(c.name)
        self.set_description(c.description)
        self.set_data_center(svc.base_link("DataCenters", c.datacenter))
        self.set_virt_service(True)
        self.set_gluster_service(False)
        self.set_trusted_service(False)
        self.set_threads_as_cores(False)
        self.set_tunnel_migration(False)
        self.set_ha_reservation(False)
        self.set_optional_reason(False)
        self.set_maintenance_reason_required(False)
        self.set_ballooning_enabled(False)

        cpu = CPU()
        cpu.set_id("IBM System z")
        cpu.set_architecture(Architecture.UNDEFINED)
        self.set_cpu(cpu)

        moc = MemoryOverCommit()
        moc.set_percent(100)
        self.set_memory_policy(sdk.MemoryPolicy(overcommit=moc))

        version = Version(major=3, minor=6)
        self.set_version(version)

    @staticmethod
    def get(parent, guid):
        for cluster in parent.get_cluster():
            if cluster.id == guid:
                return cluster
        return None

# =============================================================================

class Hosts(ProviderType, sdk.Hosts):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            pid = parent.get_id()

        coll = Hosts(parent)
        for h in hosts:
            coll.add_host(Host(coll, h))

        return coll

class Host(ProviderType, sdk.Host):
    STATDEFS = {
            "memory.total": ["Total memory", "I", "G", "B" ],
            "memory.used": ["Used memory", "I", "G", "B" ],
            "memory.free": ["Free memory", "I", "G", "B" ],
            "memory.shared": ["Shared memory", "I", "G", "B" ],
            "memory.buffers": ["IO buffers", "I", "G", "B" ],
            "memory.cached": ["OS caches", "I", "G", "B" ],
            "swap.total": ["Total swap", "I", "G", "B" ],
            "swap.free": ["Free swap", "I", "G", "B" ],
            "swap.used": ["Used swap", "I", "G", "B" ],
            "swap.cached": ["Swap also in memory", "I", "G", "B" ],
            "ksm.cpu.current": ["KSM CPU usage", "D", "G", "P" ],
            "cpu.current.user": ["User CPU usage", "D", "G", "P" ],
            "cpu.current.system": ["System CPU usage", "D", "G", "P" ],
            "cpu.current.idle": ["Idle CPU usage", "D", "G", "P" ],
            "cpu.load.avg.5m": ["CPU 5 minute load average", "D", "G", "P" ],
            "boot.time": ["Boot time of the machine", "I", "G", "N" ],
            "hugepages.1048576.free": ["Amount of free huge pages of the given size", "I", "G", "N" ],
            "hugepages.2048.free": ["Amount of free huge pages of the given size", "I", "G", "N" ],
        }

    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        h = hosts[self.id]

        self.set_status(Status(HostStatus.UP))
        self.set_name(h.name)
        self.set_description(h.description)
        self.set_status(Status(HostStatus.UP))
        self.set_external_status(Status(EntityExternalStatus.OK))
        self.set_cluster(svc.base_link("Clusters", h.cluster))
        self.set_type(HostType.RHEL)
        self.set_storage_manager(StorageManager(5, False))
        self.set_version(Version(major=3, minor=6))
        self.set_ksm(KSM(enabled=False))
        self.set_power_management(PowerManagement(enabled=False))
        self.set_live_snapshot_support(False)
        self.set_transparent_hugepages(TransparentHugePages(enabled=False))
        self.set_memory(h.memory)
        self.set_max_scheduling_memory(h.memory)
        self.set_summary(VmSummary(active=len(hosts), migrating=0, total=len(hosts)))

        t = CpuTopology()
        t.set_sockets(1)
        t.set_cores(1) #int(h.cpus))
        t.set_threads(1)
        self.set_cpu(CPU(topology=t))

    @staticmethod
    def get(parent, guid):
        for host in parent.get_host():
            if host.id == guid:
                return host
        return None

    def get_statistics(self):
        values = {
            "memory.total": hosts[self.id].memory,
            "memory.used": 0,
            "memory.free": hosts[self.id].memory,
            "swap.total": 0,
            "swap.free": 0,
            "swap.used": 0,
            "cpu.current.user": 0,
            "cpu.current.system": 0,
            "cpu.current.idle": 100,
        }
        
        host = sdk.Host(href=self.get_href(), id=self.get_id())
        stats = self.make_stats(self.STATDEFS, values, host=host)

        return stats

# =============================================================================

class StorageDomains(ProviderType, sdk.StorageDomains):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            pid = parent.get_id()

        coll = StorageDomains(parent)
        for sd in storagedomains:
            if not pid or storagedomains[sd].datacenter == pid:
                coll.add_storage_domain(StorageDomain(coll, sd))

        return coll
 
class StorageDomain(ProviderType, sdk.StorageDomain):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        sd = storagedomains[self.id]

        self.set_name(sd.name)
        self.set_description(sd.description)
        self.set_type(StorageDomainType.DATA)
        self.set_master(False)
        self.set_available(12884901888)
        self.set_used(4294967296)
        self.set_committed(0)
        self.set_storage_format(StorageFormat.V1)
        self.set_wipe_after_delete(False)
        self.set_critical_space_action_blocker(5)
        self.set_status(Status(StorageDomainStatus.ACTIVE))
        self.set_external_status(Status(EntityExternalStatus.OK))
        dcref = svc.base_link("DataCenters", sd.datacenter)
        self.set_data_center(dcref)
        self.set_data_centers(sdk.DataCenters(data_center=[dcref]))

        stg = sdk.Storage()
        stg.set_address("127.0.0.1")
        stg.set_type(StorageType.NFS)
        stg.set_path("/mnt")
        stg.set_nfs_version(NfsVersion.AUTO)
        self.set_storage(stg)

    @staticmethod
    def get(parent, guid):
        for storagedomain in parent.get_storage_domain():
            if storagedomain.id == guid:
                return storagedomain
        return None

# =============================================================================

class Disks(ProviderType, sdk.Disks):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod
    def add(obj):
        disks.add_disk(obj)
        return obj

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            if hasattr(parent, "get_disks"):
                return parent.get_disks()
            pid = parent.get_id()

        coll = Disks(parent)
        for d in disks:
            if not pid or disks[d].storagedomain == pid:
                coll.add_disk(Disk(coll, d))

        return coll

class Disk(ProviderType, sdk.Disk):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        d = disks[self.id]

        self.set_name(d.name)
        self.set_description(d.description)

    @staticmethod
    def get(parent, guid):
        for disk in parent.get_disk():
            if disk.id == guid:
                return disk
        return None

# =============================================================================

class Files(ProviderType, sdk.Files):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            if hasattr(parent, "get_files"):
                return parent.get_files()
            pid = parent.get_id()

        coll = Files(parent)
        for f in files:
            if not pid or files[f].storage_domain == pid:
                coll.add_file(File(coll, f))

        return coll

class File(ProviderType, sdk.File):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

    @staticmethod
    def get(parent, guid):
        for file in parent.get_file():
            if file.id == guid:
                return file
        return None

# =============================================================================

class Networks(ProviderType, sdk.Networks):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            if hasattr(parent, "get_networks"):
                return parent.get_networks()
            pid = parent.get_id()

        coll = Networks(parent)
        for n in networks:
            if not pid or networks[n].datacenter == pid:
                coll.add_network(Network(coll, n))

        return coll
    
class Network(ProviderType, sdk.Network):
    def __init__(self, parent, guid, *args, **kwargs):
        super().__init__(parent, guid, *args, **kwargs)

        n = networks[self.id]

        self.set_name(n.name)
        self.set_description(n.description)
        self.set_data_center(svc.base_link("DataCenters", n.datacenter))
#        self.set_cluster(svc.base_link("Clusters", n.cluster))
        self.set_status(Status(NetworkStatus.OPERATIONAL))
        self.set_display(True)
        self.set_required(True)
        self.set_mtu(0)

        u = sdk.Usages()
        u.add_usage(NetworkUsage.DISPLAY)
        u.add_usage(NetworkUsage.MIGRATION)
        u.add_usage(NetworkUsage.MANAGEMENT)
        u.add_usage(NetworkUsage.VM)
        self.set_usages(u)

    @staticmethod
    def get(parent, guid):
        for network in parent.get_network():
            if network.id == guid:
                return network
        return None

# =============================================================================

class Statistics(ProviderType, sdk.Statistics):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if hasattr(parent, "get_statistics"):
            return parent.get_statistics()

        return Statistics(parent)
    
class Statistic(ProviderType, sdk.Statistic):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod
    def get(parent, guid):
        for statistic in parent.get_statistic():
            if statistic.id == guid:
                return statistic
        return None

# =============================================================================

class Templates(ProviderType, sdk.Templates):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            if hasattr(parent, "get_templates"):
                return parent.get_templates()
            pid = parent.get_id()

        coll = Templates(parent)
        for t in templates:
            if not pid or templates[t].storage_domain == pid:
                coll.add_template(Template(coll, t))

        return coll
    
class Template(ProviderType, sdk.Template):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        t = templates[self.id]

        self.set_name(t.name)
        self.set_description(t.description)
 
        self.set_small_icon(svc.base_link("Icons", "00000000-0000-0000-0000-000000000000"))
        self.set_large_icon(svc.base_link("Icons", "00000000-0000-0000-0000-000000000000"))
        base = svc.base_link("Templates", "00000000-0000-0000-0000-000000000000")
        self.set_version(TemplateVersion(base_template=base, version_number=0))
        self.set_memory(1073741824)
        self.set_memory_policy(MemoryPolicy(1073741824))

        t = CpuTopology()
        t.set_sockets(1)
        t.set_cores(1) #int(h.cpus))
        t.set_threads(1)

        cpu = CPU()
        cpu.set_architecture(Architecture.UNDEFINED)
        cpu.set_topology(t)
        self.set_cpu(cpu)
        self.set_cpu_shares(0)
        self.set_os(OperatingSystem(OsType.OTHER))
        self.set_stateless(False)
        self.set_delete_protected(False)
        self.set_high_availability(HighAvailability(enabled=False))
        self.set_start_paused(False)

    @staticmethod
    def get(parent, guid):
        for template in parent.get_template():
            if template.id == guid:
                return template
        return None

# =============================================================================

class VMs(ProviderType, sdk.VMs):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @staticmethod    
    def get(parent, guid):
        if parent is None:
            pid = None
        else:
            if hasattr(parent, "get_vms"):
                return parent.get_vms()
            pid = parent.get_id()

        coll = VMs(parent)
        for t in vms:
#            if not pid or vms[t].storage_domain == pid:
                coll.add_template(Template(coll, t))

        return coll
    
class VM(ProviderType, sdk.VM):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        v = vms[self.id]

        self.set_name(v.name)
        self.set_description(v.description)
        self.set_description(v.description)
 
        self.set_small_icon(svc.base_link("Icons", "00000000-0000-0000-0000-000000000000"))
        self.set_large_icon(svc.base_link("Icons", "00000000-0000-0000-0000-000000000000"))
        self.set_memory(1073741824)
        self.set_memory_policy(MemoryPolicy(1073741824))

        t = CpuTopology()
        t.set_sockets(1)
        t.set_cores(1) #int(h.cpus))
        t.set_threads(1)

        cpu = CPU()
        cpu.set_architecture(Architecture.UNDEFINED)
        cpu.set_topology(t)
        self.set_cpu(cpu)
        self.set_cpu_shares(0)
        self.set_os(OperatingSystem(OsType.OTHER))
        self.set_stateless(False)
        self.set_delete_protected(False)
        self.set_high_availability(HighAvailability(enabled=False))
        self.set_start_paused(False)

    @staticmethod
    def get(parent, guid):
        return vms[guid]

