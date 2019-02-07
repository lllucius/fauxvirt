
from enum import Enum

class AccessProtocol(Enum):
    GLUSTER = 'gluster'
    NFS = 'nfs'
    CIFS = 'cifs'

class Architecture(Enum):
    UNDEFINED = 'undefined'
    X86_64 = 'x86_64'
    PPC64 = 'ppc64'

class AutoNumaStatus(Enum):
    DISABLE = 'disable'
    ENABLE = 'enable'
    UNKNOWN = 'unknown'

class BootDevice(Enum):
    CDROM = 'cdrom'
    HD = 'hd'
    NETWORK = 'network'

class BootProtocol(Enum):
    DHCP = 'dhcp'
    STATIC = 'static'
    NONE = 'none'

class ConfigurationType(Enum):
    OVF = 'ovf'

class CpuMode(Enum):
    CUSTOM = 'custom'
    HOST_MODEL = 'host_model'
    HOST_PASSTHROUGH = 'host_passthrough'

class CreationStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETE = 'complete'
    FAILED = 'failed'

class DataCenterStatus(Enum):
    UNINITIALIZED = 'uninitialized'
    UP = 'up'
    MAINTENANCE = 'maintenance'
    NOT_OPERATIONAL = 'not_operational'
    PROBLEMATIC = 'problematic'
    CONTEND = 'contend'

class DiskFormat(Enum):
    COW = 'cow'
    RAW = 'raw'

class DiskInterface(Enum):
    IDE = 'ide'
    VIRTIO_SCSI = 'virtio_scsi'
    VIRTIO = 'virtio'
    SPAPR_VSCSI = 'spapr_vscsi'

class DiskStatus(Enum):
    ILLEGAL = 'illegal'
    LOCKED = 'locked'
    OK = 'ok'

class DiskStorageType(Enum):
    IMAGE = 'image'
    LUN = 'lun'
    CINDER = 'cinder'

class DiskType(Enum):
    DATA = 'data'
    SYSTEM = 'system'

class DisplayDisconnectAction(Enum):
    NONE = 'none'
    LOCK_SCREEN = 'lock_screen'
    LOGOUT = 'logout'
    REBOOT = 'reboot'
    SHUTDOWN = 'shutdown'

class DisplayType(Enum):
    VNC = 'vnc'
    SPICE = 'spice'

class EntityExternalStatus(Enum):
    OK = 'ok'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    FAILURE = 'failure'

class ExternalSystemType(Enum):
    VDSM = 'vdsm'
    GLUSTER = 'gluster'

class FenceType(Enum):
    MANUAL = 'manual'
    RESTART = 'restart'
    START = 'start'
    STOP = 'stop'
    STATUS = 'status'

class FileType(Enum):
    ISO = 'iso'
    VFD = 'vfd'

class GlusterState(Enum):
    UP = 'up'
    DOWN = 'down'
    UNKNOWN = 'unknown'

class GlusterVolumeType(Enum):
    DISTRIBUTE = 'distribute'
    REPLICATE = 'replicate'
    DISTRIBUTED_REPLICATE = 'distributed_replicate'
    STRIPE = 'stripe'
    DISTRIBUTED_STRIPE = 'distributed_stripe'
    STRIPED_REPLICATE = 'striped_replicate'
    DISTRIBUTED_STRIPED_REPLICATE = 'distributed_striped_replicate'
    DISPERSE = 'disperse'
    DISTRIBUTED_DISPERSE = 'distributed_disperse'

class GraphicsType(Enum):
    SPICE = 'spice'
    VNC = 'vnc'

class HookContentType(Enum):
    TEXT = 'text'
    BINARY = 'binary'

class HookStage(Enum):
    PRE = 'pre'
    POST = 'post'

class HookStatus(Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    MISSING = 'missing'

class HostProtocol(Enum):
    XML = 'xml'
    STOMP = 'stomp'

class HostStatus(Enum):
    DOWN = 'down'
    ERROR = 'error'
    INITIALIZING = 'initializing'
    INSTALLING = 'installing'
    INSTALL_FAILED = 'install_failed'
    MAINTENANCE = 'maintenance'
    NON_OPERATIONAL = 'non_operational'
    NON_RESPONSIVE = 'non_responsive'
    PENDING_APPROVAL = 'pending_approval'
    PREPARING_FOR_MAINTENANCE = 'preparing_for_maintenance'
    CONNECTING = 'connecting'
    REBOOT = 'reboot'
    UNASSIGNED = 'unassigned'
    UP = 'up'
    INSTALLING_OS = 'installing_os'
    KDUMPING = 'kdumping'

class HostType(Enum):
    RHEL = 'rhel'
    RHEV_H = 'rhev_h'

class InheritableBoolean(Enum):
    TRUE = 'true'
    FALSE = 'false'
    INHERIT = 'inherit'

class IpVersion(Enum):
    V4 = 'v4'
    V6 = 'v6'

class KdumpStatus(Enum):
    UNKNOWN = 'unknown'
    DISABLED = 'disabled'
    ENABLED = 'enabled'

class LogSeverity(Enum):
    NORMAL = 'normal'
    WARNING = 'warning'
    ERROR = 'error'
    ALERT = 'alert'

class LunStatus(Enum):
    Free = 'free'
    Used = 'used'
    Unusable = 'unusable'

class MessageBrokerType(Enum):
    QPID = 'qpid'
    RABBIT_MQ = 'rabbit_mq'

class MigrateOnError(Enum):
    MIGRATE = 'migrate'
    DO_NOT_MIGRATE = 'do_not_migrate'
    MIGRATE_HIGHLY_AVAILABLE = 'migrate_highly_available'

class NetworkPluginType(Enum):
    OPEN_VSWITCH = 'open_vswitch'

class NetworkStatus(Enum):
    OPERATIONAL = 'operational'
    NON_OPERATIONAL = 'non_operational'

class NetworkUsage(Enum):
    DISPLAY = 'display'
    VM = 'vm'
    MIGRATION = 'migration'
    MANAGEMENT = 'management'

class NfsVersion(Enum):
    AUTO = 'auto'
    V3 = 'v3'
    V4 = 'v4'
    V4_1 = 'v4_1'

class NicInterface(Enum):
    E1000 = 'e1000'
    VIRTIO = 'virtio'
    RTL8139 = 'rtl8139'
    RTL8139_VIRTIO = 'rtl8139_virtio'
    SPAPR_VLAN = 'spapr_vlan'
    PCI_PASSTHROUGH = 'pci_passthrough'

class NicStatus(Enum):
    DOWN = 'down'
    UP = 'up'

class NumaTuneMode(Enum):
    STRICT = 'strict'
    INTERLEAVE = 'interleave'
    PREFERRED = 'preferred'

class OpenstackVolumeAuthenticationKeyUsageType(Enum):
    CEPH = 'ceph'

class OsType(Enum):
    UNASSIGNED = 'unassigned'
    WINDOWS_XP = 'windows_xp'
    WINDOWS_2003 = 'windows_2003'
    WINDOWS_2008 = 'windows_2008'
    OTHER_LINUX = 'other_linux'
    OTHER = 'other'
    RHEL_5 = 'rhel_5'
    RHEL_4 = 'rhel_4'
    RHEL_3 = 'rhel_3'
    WINDOWS_2003X64 = 'windows_2003x64'
    WINDOWS_7 = 'windows_7'
    WINDOWS_7X64 = 'windows_7x64'
    RHEL_5X64 = 'rhel_5x64'
    RHEL_4X64 = 'rhel_4x64'
    RHEL_3X64 = 'rhel_3x64'
    WINDOWS_2008X64 = 'windows_2008x64'
    WINDOWS_2008R2X64 = 'windows_2008r2x64'
    RHEL_6 = 'rhel_6'
    RHEL_6X64 = 'rhel_6x64'
    WINDOWS_8 = 'windows_8'
    WINDOWS_8X64 = 'windows_8x64'
    WINDOWS_2012X64 = 'windows_2012x64'

class PayloadEncoding(Enum):
    BASE64 = 'base64'
    PLAINTEXT = 'plaintext'

class PermitType(Enum):
    CREATE_VM = 'create_vm'
    DELETE_VM = 'delete_vm'
    EDIT_VM_PROPERTIES = 'edit_vm_properties'
    VM_BASIC_OPERATIONS = 'vm_basic_operations'
    REBOOT_VM = 'reboot_vm'
    STOP_VM = 'stop_vm'
    SHUT_DOWN_VM = 'shut_down_vm'
    HIBERNATE_VM = 'hibernate_vm'
    RUN_VM = 'run_vm'
    CHANGE_VM_CD = 'change_vm_cd'
    MIGRATE_VM = 'migrate_vm'
    CONNECT_TO_SERIAL_CONSOLE = 'connect_to_serial_console'
    CONNECT_TO_VM = 'connect_to_vm'
    IMPORT_EXPORT_VM = 'import_export_vm'
    CONFIGURE_VM_NETWORK = 'configure_vm_network'
    CONFIGURE_VM_STORAGE = 'configure_vm_storage'
    MOVE_VM = 'move_vm'
    MANIPULATE_VM_SNAPSHOTS = 'manipulate_vm_snapshots'
    RECONNECT_TO_VM = 'reconnect_to_vm'
    CHANGE_VM_CUSTOM_PROPERTIES = 'change_vm_custom_properties'
    EDIT_ADMIN_VM_PROPERTIES = 'edit_admin_vm_properties'
    CREATE_INSTANCE = 'create_instance'
    CREATE_HOST = 'create_host'
    EDIT_HOST_CONFIGURATION = 'edit_host_configuration'
    DELETE_HOST = 'delete_host'
    MANIPULATE_HOST = 'manipulate_host'
    CONFIGURE_HOST_NETWORK = 'configure_host_network'
    CREATE_TEMPLATE = 'create_template'
    EDIT_TEMPLATE_PROPERTIES = 'edit_template_properties'
    EDIT_ADMIN_TEMPLATE_PROPERTIES = 'edit_admin_template_properties'
    DELETE_TEMPLATE = 'delete_template'
    COPY_TEMPLATE = 'copy_template'
    CONFIGURE_TEMPLATE_NETWORK = 'configure_template_network'
    CREATE_VM_POOL = 'create_vm_pool'
    EDIT_VM_POOL_CONFIGURATION = 'edit_vm_pool_configuration'
    DELETE_VM_POOL = 'delete_vm_pool'
    VM_POOL_BASIC_OPERATIONS = 'vm_pool_basic_operations'
    CREATE_CLUSTER = 'create_cluster'
    EDIT_CLUSTER_CONFIGURATION = 'edit_cluster_configuration'
    DELETE_CLUSTER = 'delete_cluster'
    CONFIGURE_CLUSTER_NETWORK = 'configure_cluster_network'
    MANIPULATE_USERS = 'manipulate_users'
    MANIPULATE_ROLES = 'manipulate_roles'
    MANIPULATE_PERMISSIONS = 'manipulate_permissions'
    ADD_USERS_AND_GROUPS_FROM_DIRECTORY = 'add_users_and_groups_from_directory'
    EDIT_PROFILE = 'edit_profile'
    CREATE_STORAGE_DOMAIN = 'create_storage_domain'
    EDIT_STORAGE_DOMAIN_CONFIGURATION = 'edit_storage_domain_configuration'
    DELETE_STORAGE_DOMAIN = 'delete_storage_domain'
    MANIPULATE_STORAGE_DOMAIN = 'manipulate_storage_domain'
    CREATE_STORAGE_POOL = 'create_storage_pool'
    DELETE_STORAGE_POOL = 'delete_storage_pool'
    EDIT_STORAGE_POOL_CONFIGURATION = 'edit_storage_pool_configuration'
    CONFIGURE_STORAGE_POOL_NETWORK = 'configure_storage_pool_network'
    CREATE_STORAGE_POOL_NETWORK = 'create_storage_pool_network'
    DELETE_STORAGE_POOL_NETWORK = 'delete_storage_pool_network'
    ASSIGN_CLUSTER_NETWORK = 'assign_cluster_network'
    CONFIGURE_RHEVM = 'configure_rhevm'
    CONFIGURE_QUOTA = 'configure_quota'
    CONSUME_QUOTA = 'consume_quota'
    CREATE_GLUSTER_VOLUME = 'create_gluster_volume'
    MANIPULATE_GLUSTER_VOLUME = 'manipulate_gluster_volume'
    DELETE_GLUSTER_VOLUME = 'delete_gluster_volume'
    MANIPULATE_GLUSTER_HOOK = 'manipulate_gluster_hook'
    MANIPULATE_GLUSTER_SERVICE = 'manipulate_gluster_service'
    CREATE_DISK = 'create_disk'
    ATTACH_DISK = 'attach_disk'
    EDIT_DISK_PROPERTIES = 'edit_disk_properties'
    CONFIGURE_DISK_STORAGE = 'configure_disk_storage'
    DISK_LIVE_STORAGE_MIGRATION = 'disk_live_storage_migration'
    DELETE_DISK = 'delete_disk'
    CONFIGURE_SCSI_GENERIC_IO = 'configure_scsi_generic_io'
    ACCESS_IMAGE_STORAGE = 'access_image_storage'
    CREATE_CPU_PROFILE = 'create_cpu_profile'
    DELETE_CPU_PROFILE = 'delete_cpu_profile'
    UPDATE_CPU_PROFILE = 'update_cpu_profile'
    ASSIGN_CPU_PROFILE = 'assign_cpu_profile'
    CONFIGURE_NETWORK_VNIC_PROFILE = 'configure_network_vnic_profile'
    CREATE_NETWORK_VNIC_PROFILE = 'create_network_vnic_profile'
    DELETE_NETWORK_VNIC_PROFILE = 'delete_network_vnic_profile'
    LOGIN = 'login'
    INJECT_EXTERNAL_EVENTS = 'inject_external_events'
    INJECT_EXTERNAL_TASKS = 'inject_external_tasks'
    TAG_MANAGEMENT = 'tag_management'
    BOOKMARK_MANAGEMENT = 'bookmark_management'
    EVENT_NOTIFICATION_MANAGEMENT = 'event_notification_management'
    AUDIT_LOG_MANAGEMENT = 'audit_log_management'
    MANIPULATE_AFFINITY_GROUPS = 'manipulate_affinity_groups'
    CREATE_MAC_POOL = 'create_mac_pool'
    EDIT_MAC_POOL = 'edit_mac_pool'
    DELETE_MAC_POOL = 'delete_mac_pool'
    CONFIGURE_MAC_POOL = 'configure_mac_pool'
    CONFIGURE_STORAGE_DISK_PROFILE = 'configure_storage_disk_profile'
    CREATE_STORAGE_DISK_PROFILE = 'create_storage_disk_profile'
    DELETE_STORAGE_DISK_PROFILE = 'delete_storage_disk_profile'
    ATTACH_DISK_PROFILE = 'attach_disk_profile'

class PmProxyType(Enum):
    CLUSTER = 'cluster'
    DC = 'dc'
    OTHER_DC = 'other_dc'

class PolicyUnitType(Enum):
    FILTER = 'filter'
    WEIGHT = 'weight'
    LOAD_BALANCING = 'load_balancing'

class PowerManagementStatus(Enum):
    ON = 'on'
    OFF = 'off'
    UNKNOWN = 'unknown'

class QosType(Enum):
    STORAGE = 'storage'
    CPU = 'cpu'
    NETWORK = 'network'
    HOSTNETWORK = 'hostnetwork'

class QuotaModeType(Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    AUDIT = 'audit'

class ReportedDeviceType(Enum):
    NETWORK = 'network'

class ResolutionType(Enum):
    ADD = 'add'
    COPY = 'copy'

class RngSource(Enum):
    RANDOM = 'random'
    HWRNG = 'hwrng'

class RoleType(Enum):
    ADMIN = 'admin'
    USER = 'user'

class SELinuxMode(Enum):
    ENFORCING = 'enforcing'
    PERMISSIVE = 'permissive'
    DISABLED = 'disabled'

class SchedulingPolicyType(Enum):
    EVENLY_DISTRIBUTED = 'evenly_distributed'
    POWER_SAVING = 'power_saving'
    NONE = 'none'
    VM_EVENLY_DISTRIBUTED = 'vm_evenly_distributed'

class ScsiGenericIO(Enum):
    FILTERED = 'filtered'
    UNFILTERED = 'unfiltered'

class SerialNumberPolicy(Enum):
    HOST = 'host'
    VM = 'vm'
    CUSTOM = 'custom'

class SnapshotStatus(Enum):
    OK = 'ok'
    LOCKED = 'locked'
    IN_PREVIEW = 'in_preview'

class SnapshotType(Enum):
    REGULAR = 'regular'
    ACTIVE = 'active'
    STATELESS = 'stateless'
    PREVIEW = 'preview'

class SpmState(Enum):
    NONE = 'none'
    CONTENDING = 'contending'
    SPM = 'spm'

class SsoMethod(Enum):
    GUEST_AGENT = 'guest_agent'

class StepEnum(Enum):
    VALIDATING = 'validating'
    EXECUTING = 'executing'
    FINALIZING = 'finalizing'
    REBALANCING_VOLUME = 'rebalancing_volume'
    REMOVING_BRICKS = 'removing_bricks'
    UNKNOWN = 'unknown'

class StorageDomainStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    LOCKED = 'locked'
    MIXED = 'mixed'
    UNATTACHED = 'unattached'
    MAINTENANCE = 'maintenance'
    PREPARING_FOR_MAINTENANCE = 'preparing_for_maintenance'
    DETACHING = 'detaching'
    ACTIVATING = 'activating'
    UNKNOWN = 'unknown'

class StorageDomainType(Enum):
    DATA = 'data'
    ISO = 'iso'
    EXPORT = 'export'
    IMAGE = 'image'
    VOLUME = 'volume'

class StorageFormat(Enum):
    V1 = 'v1'
    V2 = 'v2'
    V3 = 'v3'

class StorageType(Enum):
    ISCSI = 'iscsi'
    FCP = 'fcp'
    NFS = 'nfs'
    LOCALFS = 'localfs'
    POSIXFS = 'posixfs'
    GLUSTERFS = 'glusterfs'
    GLANCE = 'glance'
    CINDER = 'cinder'

class TemplateStatus(Enum):
    ILLEGAL = 'illegal'
    LOCKED = 'locked'
    OK = 'ok'

class TransportType(Enum):
    TCP = 'tcp'
    RDMA = 'rdma'

class UsbType(Enum):
    LEGACY = 'legacy'
    NATIVE = 'native'

class VmAffinity(Enum):
    MIGRATABLE = 'migratable'
    USER_MIGRATABLE = 'user_migratable'
    PINNED = 'pinned'

class VmDeviceType(Enum):
    FLOPPY = 'floppy'
    CDROM = 'cdrom'

class VmPoolType(Enum):
    AUTOMATIC = 'automatic'
    MANUAL = 'manual'

class VmStatus(Enum):
    UNASSIGNED = 'unassigned'
    DOWN = 'down'
    UP = 'up'
    POWERING_UP = 'powering_up'
    PAUSED = 'paused'
    MIGRATING = 'migrating'
    UNKNOWN = 'unknown'
    NOT_RESPONDING = 'not_responding'
    WAIT_FOR_LAUNCH = 'wait_for_launch'
    REBOOT_IN_PROGRESS = 'reboot_in_progress'
    SAVING_STATE = 'saving_state'
    RESTORING_STATE = 'restoring_state'
    SUSPENDED = 'suspended'
    IMAGE_LOCKED = 'image_locked'
    POWERING_DOWN = 'powering_down'

class VmType(Enum):
    DESKTOP = 'desktop'
    SERVER = 'server'

class VnicPassThroughMode(Enum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'

class WatchdogAction(Enum):
    NONE = 'none'
    RESET = 'reset'
    POWEROFF = 'poweroff'
    PAUSE = 'pause'
    DUMP = 'dump'

class WatchdogModel(Enum):
    I6300ESB = 'i6300esb'

