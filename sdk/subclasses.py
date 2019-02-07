#!/usr/bin/env python

#
# Generated Sun Nov 18 23:21:57 2018 by generateDS.py version 2.30.5.
# Python 3.6.6 (default, Jul 19 2018, 14:25:17)  [GCC 8.1.1 20180712 (Red Hat 8.1.1-5)]
#
# Command line options:
#   ('-o', 'types.py')
#   ('--subclass-suffix', '--super=types')
#   ('-s', 'subclasses.py')
#   ('--no-namespace-defs', '')
#   ('-f', '')
#   ('-m', '')
#   ('--export', 'write')
#   ('--disable-generatedssuper-lookup', '')
#
# Command line arguments:
#   ./api.xsd
#
# Command line:
#   ./generateDS.py -o "types.py" --subclass-suffix="--super=types" -s "subclasses.py" --no-namespace-defs -f -m --export="write" --disable-generatedssuper-lookup ./api.xsd
#
# Current working directory (os.getcwd()):
#   sdk
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class KeyValuePair--super=types(supermod.KeyValuePair):
    def __init__(self, key=None, value=None, **kwargs_):
        super(KeyValuePair--super=types, self).__init__(key, value,  **kwargs_)
supermod.KeyValuePair.subclass = KeyValuePair--super=types
# end class KeyValuePair--super=types


class LinkCapabilities--super=types(supermod.LinkCapabilities):
    def __init__(self, searchable=None, **kwargs_):
        super(LinkCapabilities--super=types, self).__init__(searchable,  **kwargs_)
supermod.LinkCapabilities.subclass = LinkCapabilities--super=types
# end class LinkCapabilities--super=types


class DetailedLinks--super=types(supermod.DetailedLinks):
    def __init__(self, link=None, **kwargs_):
        super(DetailedLinks--super=types, self).__init__(link,  **kwargs_)
supermod.DetailedLinks.subclass = DetailedLinks--super=types
# end class DetailedLinks--super=types


class Link--super=types(supermod.Link):
    def __init__(self, href=None, rel=None, extensiontype_=None, **kwargs_):
        super(Link--super=types, self).__init__(href, rel, extensiontype_,  **kwargs_)
supermod.Link.subclass = Link--super=types
# end class Link--super=types


class ApiSummary--super=types(supermod.ApiSummary):
    def __init__(self, vms=None, hosts=None, users=None, storage_domains=None, **kwargs_):
        super(ApiSummary--super=types, self).__init__(vms, hosts, users, storage_domains,  **kwargs_)
supermod.ApiSummary.subclass = ApiSummary--super=types
# end class ApiSummary--super=types


class Fault--super=types(supermod.Fault):
    def __init__(self, reason=None, detail=None, **kwargs_):
        super(Fault--super=types, self).__init__(reason, detail,  **kwargs_)
supermod.Fault.subclass = Fault--super=types
# end class Fault--super=types


class UsageMessage--super=types(supermod.UsageMessage):
    def __init__(self, message=None, detailedLink=None, **kwargs_):
        super(UsageMessage--super=types, self).__init__(message, detailedLink,  **kwargs_)
supermod.UsageMessage.subclass = UsageMessage--super=types
# end class UsageMessage--super=types


class GracePeriod--super=types(supermod.GracePeriod):
    def __init__(self, expiry=None, **kwargs_):
        super(GracePeriod--super=types, self).__init__(expiry,  **kwargs_)
supermod.GracePeriod.subclass = GracePeriod--super=types
# end class GracePeriod--super=types


class IscsiDetails--super=types(supermod.IscsiDetails):
    def __init__(self, initiator=None, port=None, target=None, username=None, password=None, portal=None, address=None, serial=None, vendor_id=None, product_id=None, lun_mapping=None, size=None, paths=None, status=None, volume_group_id=None, storage_domain_id=None, disk_id=None, **kwargs_):
        super(IscsiDetails--super=types, self).__init__(initiator, port, target, username, password, portal, address, serial, vendor_id, product_id, lun_mapping, size, paths, status, volume_group_id, storage_domain_id, disk_id,  **kwargs_)
supermod.IscsiDetails.subclass = IscsiDetails--super=types
# end class IscsiDetails--super=types


class ProxyTicket--super=types(supermod.ProxyTicket):
    def __init__(self, value=None, **kwargs_):
        super(ProxyTicket--super=types, self).__init__(value,  **kwargs_)
supermod.ProxyTicket.subclass = ProxyTicket--super=types
# end class ProxyTicket--super=types


class Actions--super=types(supermod.Actions):
    def __init__(self, link=None, **kwargs_):
        super(Actions--super=types, self).__init__(link,  **kwargs_)
supermod.Actions.subclass = Actions--super=types
# end class Actions--super=types


class Status--super=types(supermod.Status):
    def __init__(self, state=None, detail=None, **kwargs_):
        super(Status--super=types, self).__init__(state, detail,  **kwargs_)
supermod.Status.subclass = Status--super=types
# end class Status--super=types


class Usages--super=types(supermod.Usages):
    def __init__(self, usage=None, **kwargs_):
        super(Usages--super=types, self).__init__(usage,  **kwargs_)
supermod.Usages.subclass = Usages--super=types
# end class Usages--super=types


class CreationStates--super=types(supermod.CreationStates):
    def __init__(self, creation_state=None, **kwargs_):
        super(CreationStates--super=types, self).__init__(creation_state,  **kwargs_)
supermod.CreationStates.subclass = CreationStates--super=types
# end class CreationStates--super=types


class Value--super=types(supermod.Value):
    def __init__(self, datum=None, detail=None, **kwargs_):
        super(Value--super=types, self).__init__(datum, detail,  **kwargs_)
supermod.Value.subclass = Value--super=types
# end class Value--super=types


class Values--super=types(supermod.Values):
    def __init__(self, type_=None, value=None, **kwargs_):
        super(Values--super=types, self).__init__(type_, value,  **kwargs_)
supermod.Values.subclass = Values--super=types
# end class Values--super=types


class CpuTopology--super=types(supermod.CpuTopology):
    def __init__(self, sockets=None, cores=None, threads=None, **kwargs_):
        super(CpuTopology--super=types, self).__init__(sockets, cores, threads,  **kwargs_)
supermod.CpuTopology.subclass = CpuTopology--super=types
# end class CpuTopology--super=types


class VCpuPin--super=types(supermod.VCpuPin):
    def __init__(self, vcpu=None, cpu_set=None, **kwargs_):
        super(VCpuPin--super=types, self).__init__(vcpu, cpu_set,  **kwargs_)
supermod.VCpuPin.subclass = VCpuPin--super=types
# end class VCpuPin--super=types


class CpuTune--super=types(supermod.CpuTune):
    def __init__(self, vcpu_pin=None, **kwargs_):
        super(CpuTune--super=types, self).__init__(vcpu_pin,  **kwargs_)
supermod.CpuTune.subclass = CpuTune--super=types
# end class CpuTune--super=types


class CPU--super=types(supermod.CPU):
    def __init__(self, id=None, topology=None, level=None, name=None, speed=None, cpu_tune=None, mode=None, architecture=None, cores=None, **kwargs_):
        super(CPU--super=types, self).__init__(id, topology, level, name, speed, cpu_tune, mode, architecture, cores,  **kwargs_)
supermod.CPU.subclass = CPU--super=types
# end class CPU--super=types


class CPUs--super=types(supermod.CPUs):
    def __init__(self, cpu=None, **kwargs_):
        super(CPUs--super=types, self).__init__(cpu,  **kwargs_)
supermod.CPUs.subclass = CPUs--super=types
# end class CPUs--super=types


class TemplateVersion--super=types(supermod.TemplateVersion):
    def __init__(self, base_template=None, version_number=None, version_name=None, **kwargs_):
        super(TemplateVersion--super=types, self).__init__(base_template, version_number, version_name,  **kwargs_)
supermod.TemplateVersion.subclass = TemplateVersion--super=types
# end class TemplateVersion--super=types


class SupportedVersions--super=types(supermod.SupportedVersions):
    def __init__(self, version=None, **kwargs_):
        super(SupportedVersions--super=types, self).__init__(version,  **kwargs_)
supermod.SupportedVersions.subclass = SupportedVersions--super=types
# end class SupportedVersions--super=types


class ErrorHandling--super=types(supermod.ErrorHandling):
    def __init__(self, on_error=None, **kwargs_):
        super(ErrorHandling--super=types, self).__init__(on_error,  **kwargs_)
supermod.ErrorHandling.subclass = ErrorHandling--super=types
# end class ErrorHandling--super=types


class Features--super=types(supermod.Features):
    def __init__(self, feature=None, **kwargs_):
        super(Features--super=types, self).__init__(feature,  **kwargs_)
supermod.Features.subclass = Features--super=types
# end class Features--super=types


class FenceTypes--super=types(supermod.FenceTypes):
    def __init__(self, fence_type=None, **kwargs_):
        super(FenceTypes--super=types, self).__init__(fence_type,  **kwargs_)
supermod.FenceTypes.subclass = FenceTypes--super=types
# end class FenceTypes--super=types


class StorageTypes--super=types(supermod.StorageTypes):
    def __init__(self, storage_type=None, **kwargs_):
        super(StorageTypes--super=types, self).__init__(storage_type,  **kwargs_)
supermod.StorageTypes.subclass = StorageTypes--super=types
# end class StorageTypes--super=types


class ConfigurationTypes--super=types(supermod.ConfigurationTypes):
    def __init__(self, configuration_type=None, **kwargs_):
        super(ConfigurationTypes--super=types, self).__init__(configuration_type,  **kwargs_)
supermod.ConfigurationTypes.subclass = ConfigurationTypes--super=types
# end class ConfigurationTypes--super=types


class StorageDomainTypes--super=types(supermod.StorageDomainTypes):
    def __init__(self, storage_domain_type=None, **kwargs_):
        super(StorageDomainTypes--super=types, self).__init__(storage_domain_type,  **kwargs_)
supermod.StorageDomainTypes.subclass = StorageDomainTypes--super=types
# end class StorageDomainTypes--super=types


class VmTypes--super=types(supermod.VmTypes):
    def __init__(self, vm_type=None, **kwargs_):
        super(VmTypes--super=types, self).__init__(vm_type,  **kwargs_)
supermod.VmTypes.subclass = VmTypes--super=types
# end class VmTypes--super=types


class BootDevices--super=types(supermod.BootDevices):
    def __init__(self, boot_device=None, **kwargs_):
        super(BootDevices--super=types, self).__init__(boot_device,  **kwargs_)
supermod.BootDevices.subclass = BootDevices--super=types
# end class BootDevices--super=types


class DisplayTypes--super=types(supermod.DisplayTypes):
    def __init__(self, display_type=None, **kwargs_):
        super(DisplayTypes--super=types, self).__init__(display_type,  **kwargs_)
supermod.DisplayTypes.subclass = DisplayTypes--super=types
# end class DisplayTypes--super=types


class NicInterfaces--super=types(supermod.NicInterfaces):
    def __init__(self, nic_interface=None, **kwargs_):
        super(NicInterfaces--super=types, self).__init__(nic_interface,  **kwargs_)
supermod.NicInterfaces.subclass = NicInterfaces--super=types
# end class NicInterfaces--super=types


class OsTypes--super=types(supermod.OsTypes):
    def __init__(self, os_type=None, **kwargs_):
        super(OsTypes--super=types, self).__init__(os_type,  **kwargs_)
supermod.OsTypes.subclass = OsTypes--super=types
# end class OsTypes--super=types


class DiskFormats--super=types(supermod.DiskFormats):
    def __init__(self, disk_format=None, **kwargs_):
        super(DiskFormats--super=types, self).__init__(disk_format,  **kwargs_)
supermod.DiskFormats.subclass = DiskFormats--super=types
# end class DiskFormats--super=types


class GraphicsTypes--super=types(supermod.GraphicsTypes):
    def __init__(self, graphics_types=None, **kwargs_):
        super(GraphicsTypes--super=types, self).__init__(graphics_types,  **kwargs_)
supermod.GraphicsTypes.subclass = GraphicsTypes--super=types
# end class GraphicsTypes--super=types


class DiskStorageTypes--super=types(supermod.DiskStorageTypes):
    def __init__(self, disk_storage_type=None, **kwargs_):
        super(DiskStorageTypes--super=types, self).__init__(disk_storage_type,  **kwargs_)
supermod.DiskStorageTypes.subclass = DiskStorageTypes--super=types
# end class DiskStorageTypes--super=types


class DiskInterfaces--super=types(supermod.DiskInterfaces):
    def __init__(self, disk_interface=None, **kwargs_):
        super(DiskInterfaces--super=types, self).__init__(disk_interface,  **kwargs_)
supermod.DiskInterfaces.subclass = DiskInterfaces--super=types
# end class DiskInterfaces--super=types


class VmAffinities--super=types(supermod.VmAffinities):
    def __init__(self, affinity=None, **kwargs_):
        super(VmAffinities--super=types, self).__init__(affinity,  **kwargs_)
supermod.VmAffinities.subclass = VmAffinities--super=types
# end class VmAffinities--super=types


class BootProtocols--super=types(supermod.BootProtocols):
    def __init__(self, boot_protocol=None, **kwargs_):
        super(BootProtocols--super=types, self).__init__(boot_protocol,  **kwargs_)
supermod.BootProtocols.subclass = BootProtocols--super=types
# end class BootProtocols--super=types


class ErrorHandlingOptions--super=types(supermod.ErrorHandlingOptions):
    def __init__(self, on_error=None, **kwargs_):
        super(ErrorHandlingOptions--super=types, self).__init__(on_error,  **kwargs_)
supermod.ErrorHandlingOptions.subclass = ErrorHandlingOptions--super=types
# end class ErrorHandlingOptions--super=types


class StorageFormats--super=types(supermod.StorageFormats):
    def __init__(self, format=None, **kwargs_):
        super(StorageFormats--super=types, self).__init__(format,  **kwargs_)
supermod.StorageFormats.subclass = StorageFormats--super=types
# end class StorageFormats--super=types


class NfsVersions--super=types(supermod.NfsVersions):
    def __init__(self, nfs_version=None, **kwargs_):
        super(NfsVersions--super=types, self).__init__(nfs_version,  **kwargs_)
supermod.NfsVersions.subclass = NfsVersions--super=types
# end class NfsVersions--super=types


class ReportedDeviceTypes--super=types(supermod.ReportedDeviceTypes):
    def __init__(self, reported_device_type=None, **kwargs_):
        super(ReportedDeviceTypes--super=types, self).__init__(reported_device_type,  **kwargs_)
supermod.ReportedDeviceTypes.subclass = ReportedDeviceTypes--super=types
# end class ReportedDeviceTypes--super=types


class IpVersions--super=types(supermod.IpVersions):
    def __init__(self, ip_version=None, **kwargs_):
        super(IpVersions--super=types, self).__init__(ip_version,  **kwargs_)
supermod.IpVersions.subclass = IpVersions--super=types
# end class IpVersions--super=types


class CpuModes--super=types(supermod.CpuModes):
    def __init__(self, cpu_mode=None, **kwargs_):
        super(CpuModes--super=types, self).__init__(cpu_mode,  **kwargs_)
supermod.CpuModes.subclass = CpuModes--super=types
# end class CpuModes--super=types


class ScsiGenericIoOptions--super=types(supermod.ScsiGenericIoOptions):
    def __init__(self, sgio_options=None, **kwargs_):
        super(ScsiGenericIoOptions--super=types, self).__init__(sgio_options,  **kwargs_)
supermod.ScsiGenericIoOptions.subclass = ScsiGenericIoOptions--super=types
# end class ScsiGenericIoOptions--super=types


class PayloadEncodings--super=types(supermod.PayloadEncodings):
    def __init__(self, payload_encodings=None, **kwargs_):
        super(PayloadEncodings--super=types, self).__init__(payload_encodings,  **kwargs_)
supermod.PayloadEncodings.subclass = PayloadEncodings--super=types
# end class PayloadEncodings--super=types


class WatchdogActions--super=types(supermod.WatchdogActions):
    def __init__(self, action=None, **kwargs_):
        super(WatchdogActions--super=types, self).__init__(action,  **kwargs_)
supermod.WatchdogActions.subclass = WatchdogActions--super=types
# end class WatchdogActions--super=types


class WatchdogModels--super=types(supermod.WatchdogModels):
    def __init__(self, model=None, **kwargs_):
        super(WatchdogModels--super=types, self).__init__(model,  **kwargs_)
supermod.WatchdogModels.subclass = WatchdogModels--super=types
# end class WatchdogModels--super=types


class SnapshotStatuses--super=types(supermod.SnapshotStatuses):
    def __init__(self, snapshot_status=None, **kwargs_):
        super(SnapshotStatuses--super=types, self).__init__(snapshot_status,  **kwargs_)
supermod.SnapshotStatuses.subclass = SnapshotStatuses--super=types
# end class SnapshotStatuses--super=types


class SsoMethods--super=types(supermod.SsoMethods):
    def __init__(self, sso_method=None, **kwargs_):
        super(SsoMethods--super=types, self).__init__(sso_method,  **kwargs_)
supermod.SsoMethods.subclass = SsoMethods--super=types
# end class SsoMethods--super=types


class KdumpStates--super=types(supermod.KdumpStates):
    def __init__(self, kdump_status=None, **kwargs_):
        super(KdumpStates--super=types, self).__init__(kdump_status,  **kwargs_)
supermod.KdumpStates.subclass = KdumpStates--super=types
# end class KdumpStates--super=types


class SpmStates--super=types(supermod.SpmStates):
    def __init__(self, spm_state=None, **kwargs_):
        super(SpmStates--super=types, self).__init__(spm_state,  **kwargs_)
supermod.SpmStates.subclass = SpmStates--super=types
# end class SpmStates--super=types


class NetworkPluginTypes--super=types(supermod.NetworkPluginTypes):
    def __init__(self, network_plugin_type=None, **kwargs_):
        super(NetworkPluginTypes--super=types, self).__init__(network_plugin_type,  **kwargs_)
supermod.NetworkPluginTypes.subclass = NetworkPluginTypes--super=types
# end class NetworkPluginTypes--super=types


class MessageBrokerTypes--super=types(supermod.MessageBrokerTypes):
    def __init__(self, message_broker_type=None, **kwargs_):
        super(MessageBrokerTypes--super=types, self).__init__(message_broker_type,  **kwargs_)
supermod.MessageBrokerTypes.subclass = MessageBrokerTypes--super=types
# end class MessageBrokerTypes--super=types


class HostStates--super=types(supermod.HostStates):
    def __init__(self, host_state=None, **kwargs_):
        super(HostStates--super=types, self).__init__(host_state,  **kwargs_)
supermod.HostStates.subclass = HostStates--super=types
# end class HostStates--super=types


class ExternalStatuses--super=types(supermod.ExternalStatuses):
    def __init__(self, external_status=None, **kwargs_):
        super(ExternalStatuses--super=types, self).__init__(external_status,  **kwargs_)
supermod.ExternalStatuses.subclass = ExternalStatuses--super=types
# end class ExternalStatuses--super=types


class QuotaModeTypes--super=types(supermod.QuotaModeTypes):
    def __init__(self, quota_mode_type=None, **kwargs_):
        super(QuotaModeTypes--super=types, self).__init__(quota_mode_type,  **kwargs_)
supermod.QuotaModeTypes.subclass = QuotaModeTypes--super=types
# end class QuotaModeTypes--super=types


class ArchitectureCapability--super=types(supermod.ArchitectureCapability):
    def __init__(self, name=None, architectures=None, **kwargs_):
        super(ArchitectureCapability--super=types, self).__init__(name, architectures,  **kwargs_)
supermod.ArchitectureCapability.subclass = ArchitectureCapability--super=types
# end class ArchitectureCapability--super=types


class ArchitectureCapabilities--super=types(supermod.ArchitectureCapabilities):
    def __init__(self, architecture_capability=None, **kwargs_):
        super(ArchitectureCapabilities--super=types, self).__init__(architecture_capability,  **kwargs_)
supermod.ArchitectureCapabilities.subclass = ArchitectureCapabilities--super=types
# end class ArchitectureCapabilities--super=types


class SerialNumberPolicies--super=types(supermod.SerialNumberPolicies):
    def __init__(self, serial_number_policy=None, **kwargs_):
        super(SerialNumberPolicies--super=types, self).__init__(serial_number_policy,  **kwargs_)
supermod.SerialNumberPolicies.subclass = SerialNumberPolicies--super=types
# end class SerialNumberPolicies--super=types


class DisplayDisconnectActions--super=types(supermod.DisplayDisconnectActions):
    def __init__(self, display_disconnect_action=None, **kwargs_):
        super(DisplayDisconnectActions--super=types, self).__init__(display_disconnect_action,  **kwargs_)
supermod.DisplayDisconnectActions.subclass = DisplayDisconnectActions--super=types
# end class DisplayDisconnectActions--super=types


class SELinuxModes--super=types(supermod.SELinuxModes):
    def __init__(self, selinux_mode=None, **kwargs_):
        super(SELinuxModes--super=types, self).__init__(selinux_mode,  **kwargs_)
supermod.SELinuxModes.subclass = SELinuxModes--super=types
# end class SELinuxModes--super=types


class SchedulingPolicyUnitTypes--super=types(supermod.SchedulingPolicyUnitTypes):
    def __init__(self, scheduling_policy_unit_type=None, **kwargs_):
        super(SchedulingPolicyUnitTypes--super=types, self).__init__(scheduling_policy_unit_type,  **kwargs_)
supermod.SchedulingPolicyUnitTypes.subclass = SchedulingPolicyUnitTypes--super=types
# end class SchedulingPolicyUnitTypes--super=types


class VmPoolTypes--super=types(supermod.VmPoolTypes):
    def __init__(self, vm_pool_type=None, **kwargs_):
        super(VmPoolTypes--super=types, self).__init__(vm_pool_type,  **kwargs_)
supermod.VmPoolTypes.subclass = VmPoolTypes--super=types
# end class VmPoolTypes--super=types


class ActionableResource--super=types(supermod.ActionableResource):
    def __init__(self, actions=None, extensiontype_=None, **kwargs_):
        super(ActionableResource--super=types, self).__init__(actions, extensiontype_,  **kwargs_)
supermod.ActionableResource.subclass = ActionableResource--super=types
# end class ActionableResource--super=types


class BaseResource--super=types(supermod.BaseResource):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, extensiontype_=None, **kwargs_):
        super(BaseResource--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, extensiontype_,  **kwargs_)
supermod.BaseResource.subclass = BaseResource--super=types
# end class BaseResource--super=types


class BaseResources--super=types(supermod.BaseResources):
    def __init__(self, actions=None, size=None, total=None, active=None, extensiontype_=None, **kwargs_):
        super(BaseResources--super=types, self).__init__(actions, size, total, active, extensiontype_,  **kwargs_)
supermod.BaseResources.subclass = BaseResources--super=types
# end class BaseResources--super=types


class Option--super=types(supermod.Option):
    def __init__(self, name=None, value=None, type_=None, **kwargs_):
        super(Option--super=types, self).__init__(name, value, type_,  **kwargs_)
supermod.Option.subclass = Option--super=types
# end class Option--super=types


class Options--super=types(supermod.Options):
    def __init__(self, option=None, **kwargs_):
        super(Options--super=types, self).__init__(option,  **kwargs_)
supermod.Options.subclass = Options--super=types
# end class Options--super=types


class InheritableBooleans--super=types(supermod.InheritableBooleans):
    def __init__(self, inheritable_boolean=None, **kwargs_):
        super(InheritableBooleans--super=types, self).__init__(inheritable_boolean,  **kwargs_)
supermod.InheritableBooleans.subclass = InheritableBooleans--super=types
# end class InheritableBooleans--super=types


class MacPool--super=types(supermod.MacPool):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, allow_duplicates=None, default_pool=None, ranges=None, **kwargs_):
        super(MacPool--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, allow_duplicates, default_pool, ranges,  **kwargs_)
supermod.MacPool.subclass = MacPool--super=types
# end class MacPool--super=types


class MacPools--super=types(supermod.MacPools):
    def __init__(self, actions=None, size=None, total=None, active=None, mac_pool=None, **kwargs_):
        super(MacPools--super=types, self).__init__(actions, size, total, active, mac_pool,  **kwargs_)
supermod.MacPools.subclass = MacPools--super=types
# end class MacPools--super=types


class Range--super=types(supermod.Range):
    def __init__(self, from_=None, to=None, **kwargs_):
        super(Range--super=types, self).__init__(from_, to,  **kwargs_)
supermod.Range.subclass = Range--super=types
# end class Range--super=types


class Ranges--super=types(supermod.Ranges):
    def __init__(self, range=None, **kwargs_):
        super(Ranges--super=types, self).__init__(range,  **kwargs_)
supermod.Ranges.subclass = Ranges--super=types
# end class Ranges--super=types


class DataCenter--super=types(supermod.DataCenter):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, storage_type=None, local=None, storage_format=None, version=None, supported_versions=None, status=None, mac_pool=None, quota_mode=None, **kwargs_):
        super(DataCenter--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, storage_type, local, storage_format, version, supported_versions, status, mac_pool, quota_mode,  **kwargs_)
supermod.DataCenter.subclass = DataCenter--super=types
# end class DataCenter--super=types


class DataCenters--super=types(supermod.DataCenters):
    def __init__(self, actions=None, size=None, total=None, active=None, data_center=None, **kwargs_):
        super(DataCenters--super=types, self).__init__(actions, size, total, active, data_center,  **kwargs_)
supermod.DataCenters.subclass = DataCenters--super=types
# end class DataCenters--super=types


class DataCenterStates--super=types(supermod.DataCenterStates):
    def __init__(self, data_center_state=None, **kwargs_):
        super(DataCenterStates--super=types, self).__init__(data_center_state,  **kwargs_)
supermod.DataCenterStates.subclass = DataCenterStates--super=types
# end class DataCenterStates--super=types


class SkipIfConnectivityBroken--super=types(supermod.SkipIfConnectivityBroken):
    def __init__(self, enabled=None, threshold=None, **kwargs_):
        super(SkipIfConnectivityBroken--super=types, self).__init__(enabled, threshold,  **kwargs_)
supermod.SkipIfConnectivityBroken.subclass = SkipIfConnectivityBroken--super=types
# end class SkipIfConnectivityBroken--super=types


class SkipIfSDActive--super=types(supermod.SkipIfSDActive):
    def __init__(self, enabled=None, **kwargs_):
        super(SkipIfSDActive--super=types, self).__init__(enabled,  **kwargs_)
supermod.SkipIfSDActive.subclass = SkipIfSDActive--super=types
# end class SkipIfSDActive--super=types


class FencingPolicy--super=types(supermod.FencingPolicy):
    def __init__(self, enabled=None, skip_if_sd_active=None, skip_if_connectivity_broken=None, **kwargs_):
        super(FencingPolicy--super=types, self).__init__(enabled, skip_if_sd_active, skip_if_connectivity_broken,  **kwargs_)
supermod.FencingPolicy.subclass = FencingPolicy--super=types
# end class FencingPolicy--super=types


class MemoryOverCommit--super=types(supermod.MemoryOverCommit):
    def __init__(self, percent=None, **kwargs_):
        super(MemoryOverCommit--super=types, self).__init__(percent,  **kwargs_)
supermod.MemoryOverCommit.subclass = MemoryOverCommit--super=types
# end class MemoryOverCommit--super=types


class MemoryPolicy--super=types(supermod.MemoryPolicy):
    def __init__(self, guaranteed=None, ballooning=None, overcommit=None, transparent_hugepages=None, **kwargs_):
        super(MemoryPolicy--super=types, self).__init__(guaranteed, ballooning, overcommit, transparent_hugepages,  **kwargs_)
supermod.MemoryPolicy.subclass = MemoryPolicy--super=types
# end class MemoryPolicy--super=types


class Console--super=types(supermod.Console):
    def __init__(self, enabled=None, **kwargs_):
        super(Console--super=types, self).__init__(enabled,  **kwargs_)
supermod.Console.subclass = Console--super=types
# end class Console--super=types


class VirtIO_SCSI--super=types(supermod.VirtIO_SCSI):
    def __init__(self, enabled=None, **kwargs_):
        super(VirtIO_SCSI--super=types, self).__init__(enabled,  **kwargs_)
supermod.VirtIO_SCSI.subclass = VirtIO_SCSI--super=types
# end class VirtIO_SCSI--super=types


class SchedulingPolicyThresholds--super=types(supermod.SchedulingPolicyThresholds):
    def __init__(self, low=None, high=None, duration=None, **kwargs_):
        super(SchedulingPolicyThresholds--super=types, self).__init__(low, high, duration,  **kwargs_)
supermod.SchedulingPolicyThresholds.subclass = SchedulingPolicyThresholds--super=types
# end class SchedulingPolicyThresholds--super=types


class SchedulingPolicyUnit--super=types(supermod.SchedulingPolicyUnit):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, internal=None, enabled=None, properties=None, **kwargs_):
        super(SchedulingPolicyUnit--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, internal, enabled, properties,  **kwargs_)
supermod.SchedulingPolicyUnit.subclass = SchedulingPolicyUnit--super=types
# end class SchedulingPolicyUnit--super=types


class SchedulingPolicyUnits--super=types(supermod.SchedulingPolicyUnits):
    def __init__(self, actions=None, size=None, total=None, active=None, scheduling_policy_unit=None, **kwargs_):
        super(SchedulingPolicyUnits--super=types, self).__init__(actions, size, total, active, scheduling_policy_unit,  **kwargs_)
supermod.SchedulingPolicyUnits.subclass = SchedulingPolicyUnits--super=types
# end class SchedulingPolicyUnits--super=types


class Filter--super=types(supermod.Filter):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, scheduling_policy_unit=None, position=None, **kwargs_):
        super(Filter--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, scheduling_policy_unit, position,  **kwargs_)
supermod.Filter.subclass = Filter--super=types
# end class Filter--super=types


class Filters--super=types(supermod.Filters):
    def __init__(self, actions=None, size=None, total=None, active=None, filter=None, **kwargs_):
        super(Filters--super=types, self).__init__(actions, size, total, active, filter,  **kwargs_)
supermod.Filters.subclass = Filters--super=types
# end class Filters--super=types


class Weight--super=types(supermod.Weight):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, scheduling_policy=None, scheduling_policy_unit=None, factor=None, **kwargs_):
        super(Weight--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, scheduling_policy, scheduling_policy_unit, factor,  **kwargs_)
supermod.Weight.subclass = Weight--super=types
# end class Weight--super=types


class Weights--super=types(supermod.Weights):
    def __init__(self, actions=None, size=None, total=None, active=None, weight=None, **kwargs_):
        super(Weights--super=types, self).__init__(actions, size, total, active, weight,  **kwargs_)
supermod.Weights.subclass = Weights--super=types
# end class Weights--super=types


class Balance--super=types(supermod.Balance):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, scheduling_policy=None, scheduling_policy_unit=None, **kwargs_):
        super(Balance--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, scheduling_policy, scheduling_policy_unit,  **kwargs_)
supermod.Balance.subclass = Balance--super=types
# end class Balance--super=types


class Balances--super=types(supermod.Balances):
    def __init__(self, actions=None, size=None, total=None, active=None, balance=None, **kwargs_):
        super(Balances--super=types, self).__init__(actions, size, total, active, balance,  **kwargs_)
supermod.Balances.subclass = Balances--super=types
# end class Balances--super=types


class SchedulingPolicy--super=types(supermod.SchedulingPolicy):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, policy=None, thresholds=None, locked=None, default_policy=None, properties=None, **kwargs_):
        super(SchedulingPolicy--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, policy, thresholds, locked, default_policy, properties,  **kwargs_)
supermod.SchedulingPolicy.subclass = SchedulingPolicy--super=types
# end class SchedulingPolicy--super=types


class Cluster--super=types(supermod.Cluster):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, cpu=None, data_center=None, memory_policy=None, scheduling_policy=None, version=None, supported_versions=None, error_handling=None, virt_service=None, gluster_service=None, threads_as_cores=None, tunnel_migration=None, trusted_service=None, ha_reservation=None, optional_reason=None, maintenance_reason_required=None, ballooning_enabled=None, display=None, ksm=None, serial_number=None, required_rng_sources=None, fencing_policy=None, migration=None, management_network=None, **kwargs_):
        super(Cluster--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, cpu, data_center, memory_policy, scheduling_policy, version, supported_versions, error_handling, virt_service, gluster_service, threads_as_cores, tunnel_migration, trusted_service, ha_reservation, optional_reason, maintenance_reason_required, ballooning_enabled, display, ksm, serial_number, required_rng_sources, fencing_policy, migration, management_network,  **kwargs_)
supermod.Cluster.subclass = Cluster--super=types
# end class Cluster--super=types


class Clusters--super=types(supermod.Clusters):
    def __init__(self, actions=None, size=None, total=None, active=None, cluster=None, **kwargs_):
        super(Clusters--super=types, self).__init__(actions, size, total, active, cluster,  **kwargs_)
supermod.Clusters.subclass = Clusters--super=types
# end class Clusters--super=types


class Agent--super=types(supermod.Agent):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, address=None, username=None, password=None, options=None, encrypt_options=None, concurrent=None, order=None, port=None, host=None, **kwargs_):
        super(Agent--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, address, username, password, options, encrypt_options, concurrent, order, port, host,  **kwargs_)
supermod.Agent.subclass = Agent--super=types
# end class Agent--super=types


class Agents--super=types(supermod.Agents):
    def __init__(self, actions=None, size=None, total=None, active=None, agent=None, **kwargs_):
        super(Agents--super=types, self).__init__(actions, size, total, active, agent,  **kwargs_)
supermod.Agents.subclass = Agents--super=types
# end class Agents--super=types


class PowerManagement--super=types(supermod.PowerManagement):
    def __init__(self, type_=None, enabled=None, address=None, username=None, password=None, options=None, status=None, pm_proxies=None, agents=None, automatic_pm_enabled=None, kdump_detection=None, **kwargs_):
        super(PowerManagement--super=types, self).__init__(type_, enabled, address, username, password, options, status, pm_proxies, agents, automatic_pm_enabled, kdump_detection,  **kwargs_)
supermod.PowerManagement.subclass = PowerManagement--super=types
# end class PowerManagement--super=types


class PowerManagementStates--super=types(supermod.PowerManagementStates):
    def __init__(self, power_management_state=None, **kwargs_):
        super(PowerManagementStates--super=types, self).__init__(power_management_state,  **kwargs_)
supermod.PowerManagementStates.subclass = PowerManagementStates--super=types
# end class PowerManagementStates--super=types


class HardwareInformation--super=types(supermod.HardwareInformation):
    def __init__(self, manufacturer=None, version=None, serial_number=None, product_name=None, uuid=None, family=None, supported_rng_sources=None, **kwargs_):
        super(HardwareInformation--super=types, self).__init__(manufacturer, version, serial_number, product_name, uuid, family, supported_rng_sources,  **kwargs_)
supermod.HardwareInformation.subclass = HardwareInformation--super=types
# end class HardwareInformation--super=types


class PowerManagers--super=types(supermod.PowerManagers):
    def __init__(self, power_management=None, **kwargs_):
        super(PowerManagers--super=types, self).__init__(power_management,  **kwargs_)
supermod.PowerManagers.subclass = PowerManagers--super=types
# end class PowerManagers--super=types


class KSM--super=types(supermod.KSM):
    def __init__(self, enabled=None, merge_across_nodes=None, **kwargs_):
        super(KSM--super=types, self).__init__(enabled, merge_across_nodes,  **kwargs_)
supermod.KSM.subclass = KSM--super=types
# end class KSM--super=types


class TransparentHugePages--super=types(supermod.TransparentHugePages):
    def __init__(self, enabled=None, **kwargs_):
        super(TransparentHugePages--super=types, self).__init__(enabled,  **kwargs_)
supermod.TransparentHugePages.subclass = TransparentHugePages--super=types
# end class TransparentHugePages--super=types


class Certificate--super=types(supermod.Certificate):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, organization=None, subject=None, content=None, **kwargs_):
        super(Certificate--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, organization, subject, content,  **kwargs_)
supermod.Certificate.subclass = Certificate--super=types
# end class Certificate--super=types


class Certificates--super=types(supermod.Certificates):
    def __init__(self, actions=None, size=None, total=None, active=None, certificate=None, **kwargs_):
        super(Certificates--super=types, self).__init__(actions, size, total, active, certificate,  **kwargs_)
supermod.Certificates.subclass = Certificates--super=types
# end class Certificates--super=types


class SELinux--super=types(supermod.SELinux):
    def __init__(self, mode=None, **kwargs_):
        super(SELinux--super=types, self).__init__(mode,  **kwargs_)
supermod.SELinux.subclass = SELinux--super=types
# end class SELinux--super=types


class VmSummary--super=types(supermod.VmSummary):
    def __init__(self, active=None, migrating=None, total=None, **kwargs_):
        super(VmSummary--super=types, self).__init__(active, migrating, total,  **kwargs_)
supermod.VmSummary.subclass = VmSummary--super=types
# end class VmSummary--super=types


class Host--super=types(supermod.Host):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, address=None, certificate=None, status=None, external_status=None, cluster=None, port=None, type_=None, storage_manager=None, spm=None, version=None, hardware_information=None, power_management=None, ksm=None, transparent_hugepages=None, iscsi=None, root_password=None, ssh=None, statistics=None, cpu=None, memory=None, max_scheduling_memory=None, summary=None, override_iptables=None, protocol=None, reboot_after_installation=None, os=None, hooks=None, libvirt_version=None, display=None, hosted_engine=None, kdump_status=None, selinux=None, auto_numa_status=None, numa_supported=None, live_snapshot_support=None, katello_errata=None, external_host_provider=None, update_available=None, device_passthrough=None, storage_connection_extensions=None, **kwargs_):
        super(Host--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, address, certificate, status, external_status, cluster, port, type_, storage_manager, spm, version, hardware_information, power_management, ksm, transparent_hugepages, iscsi, root_password, ssh, statistics, cpu, memory, max_scheduling_memory, summary, override_iptables, protocol, reboot_after_installation, os, hooks, libvirt_version, display, hosted_engine, kdump_status, selinux, auto_numa_status, numa_supported, live_snapshot_support, katello_errata, external_host_provider, update_available, device_passthrough, storage_connection_extensions,  **kwargs_)
supermod.Host.subclass = Host--super=types
# end class Host--super=types


class HostDevicePassthrough--super=types(supermod.HostDevicePassthrough):
    def __init__(self, enabled=None, **kwargs_):
        super(HostDevicePassthrough--super=types, self).__init__(enabled,  **kwargs_)
supermod.HostDevicePassthrough.subclass = HostDevicePassthrough--super=types
# end class HostDevicePassthrough--super=types


class StorageManager--super=types(supermod.StorageManager):
    def __init__(self, priority=None, valueOf_=None, **kwargs_):
        super(StorageManager--super=types, self).__init__(priority, valueOf_,  **kwargs_)
supermod.StorageManager.subclass = StorageManager--super=types
# end class StorageManager--super=types


class SPM--super=types(supermod.SPM):
    def __init__(self, priority=None, status=None, **kwargs_):
        super(SPM--super=types, self).__init__(priority, status,  **kwargs_)
supermod.SPM.subclass = SPM--super=types
# end class SPM--super=types


class HostedEngine--super=types(supermod.HostedEngine):
    def __init__(self, configured=None, active=None, score=None, global_maintenance=None, local_maintenance=None, **kwargs_):
        super(HostedEngine--super=types, self).__init__(configured, active, score, global_maintenance, local_maintenance,  **kwargs_)
supermod.HostedEngine.subclass = HostedEngine--super=types
# end class HostedEngine--super=types


class HostProtocols--super=types(supermod.HostProtocols):
    def __init__(self, host_protocol=None, **kwargs_):
        super(HostProtocols--super=types, self).__init__(host_protocol,  **kwargs_)
supermod.HostProtocols.subclass = HostProtocols--super=types
# end class HostProtocols--super=types


class HostNonOperationalDetails--super=types(supermod.HostNonOperationalDetails):
    def __init__(self, host_non_operational_detail=None, **kwargs_):
        super(HostNonOperationalDetails--super=types, self).__init__(host_non_operational_detail,  **kwargs_)
supermod.HostNonOperationalDetails.subclass = HostNonOperationalDetails--super=types
# end class HostNonOperationalDetails--super=types


class Hosts--super=types(supermod.Hosts):
    def __init__(self, actions=None, size=None, total=None, active=None, host=None, **kwargs_):
        super(Hosts--super=types, self).__init__(actions, size, total, active, host,  **kwargs_)
supermod.Hosts.subclass = Hosts--super=types
# end class Hosts--super=types


class Permit--super=types(supermod.Permit):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, administrative=None, role=None, **kwargs_):
        super(Permit--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, administrative, role,  **kwargs_)
supermod.Permit.subclass = Permit--super=types
# end class Permit--super=types


class Permits--super=types(supermod.Permits):
    def __init__(self, actions=None, size=None, total=None, active=None, permit=None, **kwargs_):
        super(Permits--super=types, self).__init__(actions, size, total, active, permit,  **kwargs_)
supermod.Permits.subclass = Permits--super=types
# end class Permits--super=types


class Role--super=types(supermod.Role):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, mutable=None, administrative=None, user=None, permits=None, **kwargs_):
        super(Role--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, mutable, administrative, user, permits,  **kwargs_)
supermod.Role.subclass = Role--super=types
# end class Role--super=types


class Roles--super=types(supermod.Roles):
    def __init__(self, actions=None, size=None, total=None, active=None, role=None, **kwargs_):
        super(Roles--super=types, self).__init__(actions, size, total, active, role,  **kwargs_)
supermod.Roles.subclass = Roles--super=types
# end class Roles--super=types


class SSHPublicKey--super=types(supermod.SSHPublicKey):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, content=None, user=None, **kwargs_):
        super(SSHPublicKey--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, content, user,  **kwargs_)
supermod.SSHPublicKey.subclass = SSHPublicKey--super=types
# end class SSHPublicKey--super=types


class SSHPublicKeys--super=types(supermod.SSHPublicKeys):
    def __init__(self, actions=None, size=None, total=None, active=None, ssh_public_key=None, **kwargs_):
        super(SSHPublicKeys--super=types, self).__init__(actions, size, total, active, ssh_public_key,  **kwargs_)
supermod.SSHPublicKeys.subclass = SSHPublicKeys--super=types
# end class SSHPublicKeys--super=types


class User--super=types(supermod.User):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, domain=None, domain_entry_id=None, department=None, logged_in=None, namespace=None, last_name=None, user_name=None, principal=None, password=None, email=None, roles=None, groups=None, **kwargs_):
        super(User--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, domain, domain_entry_id, department, logged_in, namespace, last_name, user_name, principal, password, email, roles, groups,  **kwargs_)
supermod.User.subclass = User--super=types
# end class User--super=types


class Users--super=types(supermod.Users):
    def __init__(self, actions=None, size=None, total=None, active=None, user=None, **kwargs_):
        super(Users--super=types, self).__init__(actions, size, total, active, user,  **kwargs_)
supermod.Users.subclass = Users--super=types
# end class Users--super=types


class AuthenticationMethod--super=types(supermod.AuthenticationMethod):
    def __init__(self, authentication_method=None, **kwargs_):
        super(AuthenticationMethod--super=types, self).__init__(authentication_method,  **kwargs_)
supermod.AuthenticationMethod.subclass = AuthenticationMethod--super=types
# end class AuthenticationMethod--super=types


class SSH--super=types(supermod.SSH):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, port=None, fingerprint=None, authentication_method=None, user=None, **kwargs_):
        super(SSH--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, port, fingerprint, authentication_method, user,  **kwargs_)
supermod.SSH.subclass = SSH--super=types
# end class SSH--super=types


class Group--super=types(supermod.Group):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, domain=None, domain_entry_id=None, namespace=None, roles=None, **kwargs_):
        super(Group--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, domain, domain_entry_id, namespace, roles,  **kwargs_)
supermod.Group.subclass = Group--super=types
# end class Group--super=types


class Groups--super=types(supermod.Groups):
    def __init__(self, actions=None, size=None, total=None, active=None, group=None, **kwargs_):
        super(Groups--super=types, self).__init__(actions, size, total, active, group,  **kwargs_)
supermod.Groups.subclass = Groups--super=types
# end class Groups--super=types


class Permission--super=types(supermod.Permission):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, role=None, user=None, group=None, data_center=None, cluster=None, host=None, storage_domain=None, vm=None, vmpool=None, template=None, disk=None, **kwargs_):
        super(Permission--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, role, user, group, data_center, cluster, host, storage_domain, vm, vmpool, template, disk,  **kwargs_)
supermod.Permission.subclass = Permission--super=types
# end class Permission--super=types


class Permissions--super=types(supermod.Permissions):
    def __init__(self, actions=None, size=None, total=None, active=None, permission=None, clone=None, **kwargs_):
        super(Permissions--super=types, self).__init__(actions, size, total, active, permission, clone,  **kwargs_)
supermod.Permissions.subclass = Permissions--super=types
# end class Permissions--super=types


class Domain--super=types(supermod.Domain):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, user=None, **kwargs_):
        super(Domain--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, user,  **kwargs_)
supermod.Domain.subclass = Domain--super=types
# end class Domain--super=types


class Domains--super=types(supermod.Domains):
    def __init__(self, actions=None, size=None, total=None, active=None, domain=None, **kwargs_):
        super(Domains--super=types, self).__init__(actions, size, total, active, domain,  **kwargs_)
supermod.Domains.subclass = Domains--super=types
# end class Domains--super=types


class Event--super=types(supermod.Event):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, code=None, severity=None, time=None, correlation_id=None, user=None, vm=None, storage_domain=None, host=None, template=None, cluster=None, data_center=None, origin=None, custom_id=None, flood_rate=None, custom_data=None, **kwargs_):
        super(Event--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, code, severity, time, correlation_id, user, vm, storage_domain, host, template, cluster, data_center, origin, custom_id, flood_rate, custom_data,  **kwargs_)
supermod.Event.subclass = Event--super=types
# end class Event--super=types


class Events--super=types(supermod.Events):
    def __init__(self, actions=None, size=None, total=None, active=None, event=None, **kwargs_):
        super(Events--super=types, self).__init__(actions, size, total, active, event,  **kwargs_)
supermod.Events.subclass = Events--super=types
# end class Events--super=types


class File--super=types(supermod.File):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, content=None, type_=None, storage_domain=None, **kwargs_):
        super(File--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, content, type_, storage_domain,  **kwargs_)
supermod.File.subclass = File--super=types
# end class File--super=types


class Files--super=types(supermod.Files):
    def __init__(self, actions=None, size=None, total=None, active=None, file=None, **kwargs_):
        super(Files--super=types, self).__init__(actions, size, total, active, file,  **kwargs_)
supermod.Files.subclass = Files--super=types
# end class Files--super=types


class Image--super=types(supermod.Image):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, storage_domain=None, **kwargs_):
        super(Image--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, storage_domain,  **kwargs_)
supermod.Image.subclass = Image--super=types
# end class Image--super=types


class Images--super=types(supermod.Images):
    def __init__(self, actions=None, size=None, total=None, active=None, image=None, **kwargs_):
        super(Images--super=types, self).__init__(actions, size, total, active, image,  **kwargs_)
supermod.Images.subclass = Images--super=types
# end class Images--super=types


class Hook--super=types(supermod.Hook):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, event_name=None, md5=None, host=None, **kwargs_):
        super(Hook--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, event_name, md5, host,  **kwargs_)
supermod.Hook.subclass = Hook--super=types
# end class Hook--super=types


class Hooks--super=types(supermod.Hooks):
    def __init__(self, actions=None, size=None, total=None, active=None, hook=None, **kwargs_):
        super(Hooks--super=types, self).__init__(actions, size, total, active, hook,  **kwargs_)
supermod.Hooks.subclass = Hooks--super=types
# end class Hooks--super=types


class IP--super=types(supermod.IP):
    def __init__(self, address=None, netmask=None, gateway=None, version=None, **kwargs_):
        super(IP--super=types, self).__init__(address, netmask, gateway, version,  **kwargs_)
supermod.IP.subclass = IP--super=types
# end class IP--super=types


class IPs--super=types(supermod.IPs):
    def __init__(self, actions=None, size=None, total=None, active=None, ip=None, **kwargs_):
        super(IPs--super=types, self).__init__(actions, size, total, active, ip,  **kwargs_)
supermod.IPs.subclass = IPs--super=types
# end class IPs--super=types


class MAC--super=types(supermod.MAC):
    def __init__(self, address=None, **kwargs_):
        super(MAC--super=types, self).__init__(address,  **kwargs_)
supermod.MAC.subclass = MAC--super=types
# end class MAC--super=types


class VLAN--super=types(supermod.VLAN):
    def __init__(self, id=None, **kwargs_):
        super(VLAN--super=types, self).__init__(id,  **kwargs_)
supermod.VLAN.subclass = VLAN--super=types
# end class VLAN--super=types


class Network--super=types(supermod.Network):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, data_center=None, cluster=None, ip=None, vlan=None, stp=None, status=None, display=None, mtu=None, usages=None, required=None, profile_required=None, labels=None, qos=None, **kwargs_):
        super(Network--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, data_center, cluster, ip, vlan, stp, status, display, mtu, usages, required, profile_required, labels, qos,  **kwargs_)
supermod.Network.subclass = Network--super=types
# end class Network--super=types


class NetworkStates--super=types(supermod.NetworkStates):
    def __init__(self, network_state=None, **kwargs_):
        super(NetworkStates--super=types, self).__init__(network_state,  **kwargs_)
supermod.NetworkStates.subclass = NetworkStates--super=types
# end class NetworkStates--super=types


class Networks--super=types(supermod.Networks):
    def __init__(self, actions=None, size=None, total=None, active=None, network=None, **kwargs_):
        super(Networks--super=types, self).__init__(actions, size, total, active, network,  **kwargs_)
supermod.Networks.subclass = Networks--super=types
# end class Networks--super=types


class Label--super=types(supermod.Label):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, network=None, host_nic=None, **kwargs_):
        super(Label--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, network, host_nic,  **kwargs_)
supermod.Label.subclass = Label--super=types
# end class Label--super=types


class Labels--super=types(supermod.Labels):
    def __init__(self, actions=None, size=None, total=None, active=None, label=None, **kwargs_):
        super(Labels--super=types, self).__init__(actions, size, total, active, label,  **kwargs_)
supermod.Labels.subclass = Labels--super=types
# end class Labels--super=types


class VnicProfile--super=types(supermod.VnicProfile):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, network=None, port_mirroring=None, custom_properties=None, pass_through=None, qos=None, **kwargs_):
        super(VnicProfile--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, network, port_mirroring, custom_properties, pass_through, qos,  **kwargs_)
supermod.VnicProfile.subclass = VnicProfile--super=types
# end class VnicProfile--super=types


class VnicProfiles--super=types(supermod.VnicProfiles):
    def __init__(self, actions=None, size=None, total=None, active=None, vnic_profile=None, **kwargs_):
        super(VnicProfiles--super=types, self).__init__(actions, size, total, active, vnic_profile,  **kwargs_)
supermod.VnicProfiles.subclass = VnicProfiles--super=types
# end class VnicProfiles--super=types


class VnicPassThrough--super=types(supermod.VnicPassThrough):
    def __init__(self, mode=None, **kwargs_):
        super(VnicPassThrough--super=types, self).__init__(mode,  **kwargs_)
supermod.VnicPassThrough.subclass = VnicPassThrough--super=types
# end class VnicPassThrough--super=types


class StorageConnectionExtensions--super=types(supermod.StorageConnectionExtensions):
    def __init__(self, actions=None, size=None, total=None, active=None, storage_connection_extension=None, **kwargs_):
        super(StorageConnectionExtensions--super=types, self).__init__(actions, size, total, active, storage_connection_extension,  **kwargs_)
supermod.StorageConnectionExtensions.subclass = StorageConnectionExtensions--super=types
# end class StorageConnectionExtensions--super=types


class StorageConnectionExtension--super=types(supermod.StorageConnectionExtension):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, target=None, username=None, password=None, host=None, **kwargs_):
        super(StorageConnectionExtension--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, target, username, password, host,  **kwargs_)
supermod.StorageConnectionExtension.subclass = StorageConnectionExtension--super=types
# end class StorageConnectionExtension--super=types


class LogicalUnit--super=types(supermod.LogicalUnit):
    def __init__(self, id=None, port=None, target=None, username=None, password=None, portal=None, address=None, serial=None, vendor_id=None, product_id=None, lun_mapping=None, size=None, paths=None, status=None, volume_group_id=None, storage_domain_id=None, disk_id=None, **kwargs_):
        super(LogicalUnit--super=types, self).__init__(id, port, target, username, password, portal, address, serial, vendor_id, product_id, lun_mapping, size, paths, status, volume_group_id, storage_domain_id, disk_id,  **kwargs_)
supermod.LogicalUnit.subclass = LogicalUnit--super=types
# end class LogicalUnit--super=types


class LogicalUnits--super=types(supermod.LogicalUnits):
    def __init__(self, actions=None, size=None, total=None, active=None, logical_unit=None, **kwargs_):
        super(LogicalUnits--super=types, self).__init__(actions, size, total, active, logical_unit,  **kwargs_)
supermod.LogicalUnits.subclass = LogicalUnits--super=types
# end class LogicalUnits--super=types


class VolumeGroup--super=types(supermod.VolumeGroup):
    def __init__(self, id=None, name=None, logical_unit=None, **kwargs_):
        super(VolumeGroup--super=types, self).__init__(id, name, logical_unit,  **kwargs_)
supermod.VolumeGroup.subclass = VolumeGroup--super=types
# end class VolumeGroup--super=types


class Storage--super=types(supermod.Storage):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, address=None, type_=None, path=None, mount_options=None, vfs_type=None, nfs_version=None, nfs_timeo=None, nfs_retrans=None, logical_unit=None, volume_group=None, override_luns=None, port=None, target=None, username=None, password=None, portal=None, host=None, **kwargs_):
        super(Storage--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, address, type_, path, mount_options, vfs_type, nfs_version, nfs_timeo, nfs_retrans, logical_unit, volume_group, override_luns, port, target, username, password, portal, host,  **kwargs_)
supermod.Storage.subclass = Storage--super=types
# end class Storage--super=types


class StorageConnection--super=types(supermod.StorageConnection):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, address=None, type_=None, path=None, mount_options=None, vfs_type=None, nfs_version=None, nfs_timeo=None, nfs_retrans=None, port=None, target=None, username=None, password=None, portal=None, host=None, **kwargs_):
        super(StorageConnection--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, address, type_, path, mount_options, vfs_type, nfs_version, nfs_timeo, nfs_retrans, port, target, username, password, portal, host,  **kwargs_)
supermod.StorageConnection.subclass = StorageConnection--super=types
# end class StorageConnection--super=types


class StorageDomain--super=types(supermod.StorageDomain):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, data_center=None, data_centers=None, type_=None, status=None, external_status=None, master=None, storage=None, host=None, format=None, destroy=None, available=None, used=None, committed=None, storage_format=None, wipe_after_delete=None, import_=None, warning_low_space_indicator=None, critical_space_action_blocker=None, **kwargs_):
        super(StorageDomain--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, data_center, data_centers, type_, status, external_status, master, storage, host, format, destroy, available, used, committed, storage_format, wipe_after_delete, import_, warning_low_space_indicator, critical_space_action_blocker,  **kwargs_)
supermod.StorageDomain.subclass = StorageDomain--super=types
# end class StorageDomain--super=types


class StorageDomainStates--super=types(supermod.StorageDomainStates):
    def __init__(self, storage_domain_state=None, **kwargs_):
        super(StorageDomainStates--super=types, self).__init__(storage_domain_state,  **kwargs_)
supermod.StorageDomainStates.subclass = StorageDomainStates--super=types
# end class StorageDomainStates--super=types


class StorageDomains--super=types(supermod.StorageDomains):
    def __init__(self, actions=None, size=None, total=None, active=None, storage_domain=None, **kwargs_):
        super(StorageDomains--super=types, self).__init__(actions, size, total, active, storage_domain,  **kwargs_)
supermod.StorageDomains.subclass = StorageDomains--super=types
# end class StorageDomains--super=types


class StorageConnections--super=types(supermod.StorageConnections):
    def __init__(self, actions=None, size=None, total=None, active=None, storage_connection=None, **kwargs_):
        super(StorageConnections--super=types, self).__init__(actions, size, total, active, storage_connection,  **kwargs_)
supermod.StorageConnections.subclass = StorageConnections--super=types
# end class StorageConnections--super=types


class InstanceTypes--super=types(supermod.InstanceTypes):
    def __init__(self, actions=None, size=None, total=None, active=None, instance_type=None, **kwargs_):
        super(InstanceTypes--super=types, self).__init__(actions, size, total, active, instance_type,  **kwargs_)
supermod.InstanceTypes.subclass = InstanceTypes--super=types
# end class InstanceTypes--super=types


class Templates--super=types(supermod.Templates):
    def __init__(self, actions=None, size=None, total=None, active=None, template=None, **kwargs_):
        super(Templates--super=types, self).__init__(actions, size, total, active, template,  **kwargs_)
supermod.Templates.subclass = Templates--super=types
# end class Templates--super=types


class TemplateStates--super=types(supermod.TemplateStates):
    def __init__(self, template_state=None, **kwargs_):
        super(TemplateStates--super=types, self).__init__(template_state,  **kwargs_)
supermod.TemplateStates.subclass = TemplateStates--super=types
# end class TemplateStates--super=types


class Bios--super=types(supermod.Bios):
    def __init__(self, boot_menu=None, **kwargs_):
        super(Bios--super=types, self).__init__(boot_menu,  **kwargs_)
supermod.Bios.subclass = Bios--super=types
# end class Bios--super=types


class BootMenu--super=types(supermod.BootMenu):
    def __init__(self, enabled=None, **kwargs_):
        super(BootMenu--super=types, self).__init__(enabled,  **kwargs_)
supermod.BootMenu.subclass = BootMenu--super=types
# end class BootMenu--super=types


class Boot--super=types(supermod.Boot):
    def __init__(self, dev=None, **kwargs_):
        super(Boot--super=types, self).__init__(dev,  **kwargs_)
supermod.Boot.subclass = Boot--super=types
# end class Boot--super=types


class OperatingSystem--super=types(supermod.OperatingSystem):
    def __init__(self, type_=None, boot=None, kernel=None, initrd=None, cmdline=None, version=None, **kwargs_):
        super(OperatingSystem--super=types, self).__init__(type_, boot, kernel, initrd, cmdline, version,  **kwargs_)
supermod.OperatingSystem.subclass = OperatingSystem--super=types
# end class OperatingSystem--super=types


class Sso--super=types(supermod.Sso):
    def __init__(self, methods=None, **kwargs_):
        super(Sso--super=types, self).__init__(methods,  **kwargs_)
supermod.Sso.subclass = Sso--super=types
# end class Sso--super=types


class Methods--super=types(supermod.Methods):
    def __init__(self, method=None, **kwargs_):
        super(Methods--super=types, self).__init__(method,  **kwargs_)
supermod.Methods.subclass = Methods--super=types
# end class Methods--super=types


class Method--super=types(supermod.Method):
    def __init__(self, id=None, **kwargs_):
        super(Method--super=types, self).__init__(id,  **kwargs_)
supermod.Method.subclass = Method--super=types
# end class Method--super=types


class Rate--super=types(supermod.Rate):
    def __init__(self, bytes=None, period=None, **kwargs_):
        super(Rate--super=types, self).__init__(bytes, period,  **kwargs_)
supermod.Rate.subclass = Rate--super=types
# end class Rate--super=types


class RngSources--super=types(supermod.RngSources):
    def __init__(self, source=None, **kwargs_):
        super(RngSources--super=types, self).__init__(source,  **kwargs_)
supermod.RngSources.subclass = RngSources--super=types
# end class RngSources--super=types


class RngDevice--super=types(supermod.RngDevice):
    def __init__(self, rate=None, source=None, **kwargs_):
        super(RngDevice--super=types, self).__init__(rate, source,  **kwargs_)
supermod.RngDevice.subclass = RngDevice--super=types
# end class RngDevice--super=types


class HighAvailability--super=types(supermod.HighAvailability):
    def __init__(self, enabled=None, priority=None, **kwargs_):
        super(HighAvailability--super=types, self).__init__(enabled, priority,  **kwargs_)
supermod.HighAvailability.subclass = HighAvailability--super=types
# end class HighAvailability--super=types


class Display--super=types(supermod.Display):
    def __init__(self, type_=None, address=None, port=None, secure_port=None, monitors=None, single_qxl_pci=None, allow_override=None, certificate=None, smartcard_enabled=None, keyboard_layout=None, proxy=None, file_transfer_enabled=None, copy_paste_enabled=None, disconnect_action=None, **kwargs_):
        super(Display--super=types, self).__init__(type_, address, port, secure_port, monitors, single_qxl_pci, allow_override, certificate, smartcard_enabled, keyboard_layout, proxy, file_transfer_enabled, copy_paste_enabled, disconnect_action,  **kwargs_)
supermod.Display.subclass = Display--super=types
# end class Display--super=types


class GraphicsConsoles--super=types(supermod.GraphicsConsoles):
    def __init__(self, actions=None, size=None, total=None, active=None, graphics_console=None, **kwargs_):
        super(GraphicsConsoles--super=types, self).__init__(actions, size, total, active, graphics_console,  **kwargs_)
supermod.GraphicsConsoles.subclass = GraphicsConsoles--super=types
# end class GraphicsConsoles--super=types


class GraphicsConsole--super=types(supermod.GraphicsConsole):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, vm=None, template=None, instance_type=None, protocol=None, port=None, tls_port=None, address=None, **kwargs_):
        super(GraphicsConsole--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, vm, template, instance_type, protocol, port, tls_port, address,  **kwargs_)
supermod.GraphicsConsole.subclass = GraphicsConsole--super=types
# end class GraphicsConsole--super=types


class Ticket--super=types(supermod.Ticket):
    def __init__(self, value=None, expiry=None, **kwargs_):
        super(Ticket--super=types, self).__init__(value, expiry,  **kwargs_)
supermod.Ticket.subclass = Ticket--super=types
# end class Ticket--super=types


class CustomProperty--super=types(supermod.CustomProperty):
    def __init__(self, name=None, value=None, regexp=None, **kwargs_):
        super(CustomProperty--super=types, self).__init__(name, value, regexp,  **kwargs_)
supermod.CustomProperty.subclass = CustomProperty--super=types
# end class CustomProperty--super=types


class CustomProperties--super=types(supermod.CustomProperties):
    def __init__(self, custom_property=None, **kwargs_):
        super(CustomProperties--super=types, self).__init__(custom_property,  **kwargs_)
supermod.CustomProperties.subclass = CustomProperties--super=types
# end class CustomProperties--super=types


class Property--super=types(supermod.Property):
    def __init__(self, name=None, value=None, **kwargs_):
        super(Property--super=types, self).__init__(name, value,  **kwargs_)
supermod.Property.subclass = Property--super=types
# end class Property--super=types


class Properties--super=types(supermod.Properties):
    def __init__(self, property=None, **kwargs_):
        super(Properties--super=types, self).__init__(property,  **kwargs_)
supermod.Properties.subclass = Properties--super=types
# end class Properties--super=types


class Payloads--super=types(supermod.Payloads):
    def __init__(self, payload=None, **kwargs_):
        super(Payloads--super=types, self).__init__(payload,  **kwargs_)
supermod.Payloads.subclass = Payloads--super=types
# end class Payloads--super=types


class Payload--super=types(supermod.Payload):
    def __init__(self, type_=None, files=None, volume_id=None, **kwargs_):
        super(Payload--super=types, self).__init__(type_, files, volume_id,  **kwargs_)
supermod.Payload.subclass = Payload--super=types
# end class Payload--super=types


class VmDeviceTypes--super=types(supermod.VmDeviceTypes):
    def __init__(self, vm_device_types=None, **kwargs_):
        super(VmDeviceTypes--super=types, self).__init__(vm_device_types,  **kwargs_)
supermod.VmDeviceTypes.subclass = VmDeviceTypes--super=types
# end class VmDeviceTypes--super=types


class Configuration--super=types(supermod.Configuration):
    def __init__(self, type_=None, data=None, **kwargs_):
        super(Configuration--super=types, self).__init__(type_, data,  **kwargs_)
supermod.Configuration.subclass = Configuration--super=types
# end class Configuration--super=types


class Initialization--super=types(supermod.Initialization):
    def __init__(self, configuration=None, cloud_init=None, host_name=None, domain=None, timezone=None, authorized_ssh_keys=None, regenerate_ssh_keys=None, regenerate_ids=None, dns_servers=None, dns_search=None, nic_configurations=None, windows_license_key=None, root_password=None, custom_script=None, input_locale=None, ui_language=None, system_locale=None, user_locale=None, user_name=None, active_directory_ou=None, org_name=None, **kwargs_):
        super(Initialization--super=types, self).__init__(configuration, cloud_init, host_name, domain, timezone, authorized_ssh_keys, regenerate_ssh_keys, regenerate_ids, dns_servers, dns_search, nic_configurations, windows_license_key, root_password, custom_script, input_locale, ui_language, system_locale, user_locale, user_name, active_directory_ou, org_name,  **kwargs_)
supermod.Initialization.subclass = Initialization--super=types
# end class Initialization--super=types


class DNS--super=types(supermod.DNS):
    def __init__(self, servers=None, search_domains=None, **kwargs_):
        super(DNS--super=types, self).__init__(servers, search_domains,  **kwargs_)
supermod.DNS.subclass = DNS--super=types
# end class DNS--super=types


class AuthorizedKey--super=types(supermod.AuthorizedKey):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, user=None, key=None, **kwargs_):
        super(AuthorizedKey--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, user, key,  **kwargs_)
supermod.AuthorizedKey.subclass = AuthorizedKey--super=types
# end class AuthorizedKey--super=types


class AuthorizedKeys--super=types(supermod.AuthorizedKeys):
    def __init__(self, actions=None, size=None, total=None, active=None, authorized_key=None, **kwargs_):
        super(AuthorizedKeys--super=types, self).__init__(actions, size, total, active, authorized_key,  **kwargs_)
supermod.AuthorizedKeys.subclass = AuthorizedKeys--super=types
# end class AuthorizedKeys--super=types


class CloudInit--super=types(supermod.CloudInit):
    def __init__(self, host=None, authorized_keys=None, network_configuration=None, regenerate_ssh_keys=None, timezone=None, users=None, files=None, **kwargs_):
        super(CloudInit--super=types, self).__init__(host, authorized_keys, network_configuration, regenerate_ssh_keys, timezone, users, files,  **kwargs_)
supermod.CloudInit.subclass = CloudInit--super=types
# end class CloudInit--super=types


class NetworkConfiguration--super=types(supermod.NetworkConfiguration):
    def __init__(self, nics=None, dns=None, **kwargs_):
        super(NetworkConfiguration--super=types, self).__init__(nics, dns,  **kwargs_)
supermod.NetworkConfiguration.subclass = NetworkConfiguration--super=types
# end class NetworkConfiguration--super=types


class VmPlacementPolicy--super=types(supermod.VmPlacementPolicy):
    def __init__(self, hosts=None, host=None, affinity=None, **kwargs_):
        super(VmPlacementPolicy--super=types, self).__init__(hosts, host, affinity,  **kwargs_)
supermod.VmPlacementPolicy.subclass = VmPlacementPolicy--super=types
# end class VmPlacementPolicy--super=types


class TimeZone--super=types(supermod.TimeZone):
    def __init__(self, name=None, utc_offset=None, **kwargs_):
        super(TimeZone--super=types, self).__init__(name, utc_offset,  **kwargs_)
supermod.TimeZone.subclass = TimeZone--super=types
# end class TimeZone--super=types


class Kernel--super=types(supermod.Kernel):
    def __init__(self, version=None, **kwargs_):
        super(Kernel--super=types, self).__init__(version,  **kwargs_)
supermod.Kernel.subclass = Kernel--super=types
# end class Kernel--super=types


class GuestOperatingSystem--super=types(supermod.GuestOperatingSystem):
    def __init__(self, architecture=None, codename=None, distribution=None, kernel=None, family=None, version=None, **kwargs_):
        super(GuestOperatingSystem--super=types, self).__init__(architecture, codename, distribution, kernel, family, version,  **kwargs_)
supermod.GuestOperatingSystem.subclass = GuestOperatingSystem--super=types
# end class GuestOperatingSystem--super=types


class GuestInfo--super=types(supermod.GuestInfo):
    def __init__(self, ips=None, fqdn=None, **kwargs_):
        super(GuestInfo--super=types, self).__init__(ips, fqdn,  **kwargs_)
supermod.GuestInfo.subclass = GuestInfo--super=types
# end class GuestInfo--super=types


class SerialNumber--super=types(supermod.SerialNumber):
    def __init__(self, policy=None, value=None, **kwargs_):
        super(SerialNumber--super=types, self).__init__(policy, value,  **kwargs_)
supermod.SerialNumber.subclass = SerialNumber--super=types
# end class SerialNumber--super=types


class MigrationOptions--super=types(supermod.MigrationOptions):
    def __init__(self, auto_converge=None, compressed=None, **kwargs_):
        super(MigrationOptions--super=types, self).__init__(auto_converge, compressed,  **kwargs_)
supermod.MigrationOptions.subclass = MigrationOptions--super=types
# end class MigrationOptions--super=types


class IO--super=types(supermod.IO):
    def __init__(self, threads=None, **kwargs_):
        super(IO--super=types, self).__init__(threads,  **kwargs_)
supermod.IO.subclass = IO--super=types
# end class IO--super=types


class VmBase--super=types(supermod.VmBase):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, status=None, memory=None, cpu=None, cpu_shares=None, bios=None, os=None, cluster=None, storage_domain=None, creation_time=None, origin=None, stateless=None, delete_protected=None, high_availability=None, display=None, sso=None, rng_device=None, console=None, timezone=None, domain=None, usb=None, soundcard_enabled=None, tunnel_migration=None, migration_downtime=None, virtio_scsi=None, serial_number=None, start_paused=None, cpu_profile=None, migration=None, io=None, custom_properties=None, custom_emulated_machine=None, custom_cpu_model=None, time_zone=None, small_icon=None, large_icon=None, memory_policy=None, extensiontype_=None, **kwargs_):
        super(VmBase--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, status, memory, cpu, cpu_shares, bios, os, cluster, storage_domain, creation_time, origin, stateless, delete_protected, high_availability, display, sso, rng_device, console, timezone, domain, usb, soundcard_enabled, tunnel_migration, migration_downtime, virtio_scsi, serial_number, start_paused, cpu_profile, migration, io, custom_properties, custom_emulated_machine, custom_cpu_model, time_zone, small_icon, large_icon, memory_policy, extensiontype_,  **kwargs_)
supermod.VmBase.subclass = VmBase--super=types
# end class VmBase--super=types


class VM--super=types(supermod.VM):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, status=None, memory=None, cpu=None, cpu_shares=None, bios=None, os=None, cluster=None, storage_domain=None, creation_time=None, origin=None, stateless=None, delete_protected=None, high_availability=None, display=None, sso=None, rng_device=None, console=None, timezone=None, domain=None, usb=None, soundcard_enabled=None, tunnel_migration=None, migration_downtime=None, virtio_scsi=None, serial_number=None, start_paused=None, cpu_profile=None, migration=None, io=None, custom_properties=None, custom_emulated_machine=None, custom_cpu_model=None, time_zone=None, small_icon=None, large_icon=None, memory_policy=None, stop_reason=None, host=None, template=None, instance_type=None, start_time=None, stop_time=None, run_once=None, payloads=None, statistics=None, disks=None, initialization=None, nics=None, tags=None, snapshots=None, placement_policy=None, guest_info=None, quota=None, vmpool=None, cdroms=None, floppies=None, reported_devices=None, watchdogs=None, use_latest_template_version=None, next_run_configuration_exists=None, numa_tune_mode=None, permissions=None, external_host_provider=None, katello_errata=None, guest_time_zone=None, guest_operating_system=None, extensiontype_=None, **kwargs_):
        super(VM--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, status, memory, cpu, cpu_shares, bios, os, cluster, storage_domain, creation_time, origin, stateless, delete_protected, high_availability, display, sso, rng_device, console, timezone, domain, usb, soundcard_enabled, tunnel_migration, migration_downtime, virtio_scsi, serial_number, start_paused, cpu_profile, migration, io, custom_properties, custom_emulated_machine, custom_cpu_model, time_zone, small_icon, large_icon, memory_policy, stop_reason, host, template, instance_type, start_time, stop_time, run_once, payloads, statistics, disks, initialization, nics, tags, snapshots, placement_policy, guest_info, quota, vmpool, cdroms, floppies, reported_devices, watchdogs, use_latest_template_version, next_run_configuration_exists, numa_tune_mode, permissions, external_host_provider, katello_errata, guest_time_zone, guest_operating_system, extensiontype_,  **kwargs_)
supermod.VM.subclass = VM--super=types
# end class VM--super=types


class VMs--super=types(supermod.VMs):
    def __init__(self, actions=None, size=None, total=None, active=None, vm=None, **kwargs_):
        super(VMs--super=types, self).__init__(actions, size, total, active, vm,  **kwargs_)
supermod.VMs.subclass = VMs--super=types
# end class VMs--super=types


class Icon--super=types(supermod.Icon):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, media_type=None, data=None, **kwargs_):
        super(Icon--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, media_type, data,  **kwargs_)
supermod.Icon.subclass = Icon--super=types
# end class Icon--super=types


class Icons--super=types(supermod.Icons):
    def __init__(self, actions=None, size=None, total=None, active=None, icon=None, **kwargs_):
        super(Icons--super=types, self).__init__(actions, size, total, active, icon,  **kwargs_)
supermod.Icons.subclass = Icons--super=types
# end class Icons--super=types


class ReportedDevices--super=types(supermod.ReportedDevices):
    def __init__(self, actions=None, size=None, total=None, active=None, reported_device=None, **kwargs_):
        super(ReportedDevices--super=types, self).__init__(actions, size, total, active, reported_device,  **kwargs_)
supermod.ReportedDevices.subclass = ReportedDevices--super=types
# end class ReportedDevices--super=types


class ReportedDevice--super=types(supermod.ReportedDevice):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, mac=None, ips=None, vm=None, **kwargs_):
        super(ReportedDevice--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, mac, ips, vm,  **kwargs_)
supermod.ReportedDevice.subclass = ReportedDevice--super=types
# end class ReportedDevice--super=types


class PreviewVMs--super=types(supermod.PreviewVMs):
    def __init__(self, actions=None, size=None, total=None, active=None, preview_vm=None, **kwargs_):
        super(PreviewVMs--super=types, self).__init__(actions, size, total, active, preview_vm,  **kwargs_)
supermod.PreviewVMs.subclass = PreviewVMs--super=types
# end class PreviewVMs--super=types


class VmStates--super=types(supermod.VmStates):
    def __init__(self, vm_state=None, **kwargs_):
        super(VmStates--super=types, self).__init__(vm_state,  **kwargs_)
supermod.VmStates.subclass = VmStates--super=types
# end class VmStates--super=types


class VmPauseDetails--super=types(supermod.VmPauseDetails):
    def __init__(self, vm_pause_detail=None, **kwargs_):
        super(VmPauseDetails--super=types, self).__init__(vm_pause_detail,  **kwargs_)
supermod.VmPauseDetails.subclass = VmPauseDetails--super=types
# end class VmPauseDetails--super=types


class PmProxyTypes--super=types(supermod.PmProxyTypes):
    def __init__(self, type_=None, **kwargs_):
        super(PmProxyTypes--super=types, self).__init__(type_,  **kwargs_)
supermod.PmProxyTypes.subclass = PmProxyTypes--super=types
# end class PmProxyTypes--super=types


class Session--super=types(supermod.Session):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, vm=None, protocol=None, ip=None, user=None, console_user=None, **kwargs_):
        super(Session--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, vm, protocol, ip, user, console_user,  **kwargs_)
supermod.Session.subclass = Session--super=types
# end class Session--super=types


class Sessions--super=types(supermod.Sessions):
    def __init__(self, actions=None, size=None, total=None, active=None, session=None, **kwargs_):
        super(Sessions--super=types, self).__init__(actions, size, total, active, session,  **kwargs_)
supermod.Sessions.subclass = Sessions--super=types
# end class Sessions--super=types


class VmPool--super=types(supermod.VmPool):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, size=None, cluster=None, template=None, vm=None, prestarted_vms=None, max_user_vms=None, display=None, rng_device=None, soundcard_enabled=None, type_=None, use_latest_template_version=None, **kwargs_):
        super(VmPool--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, size, cluster, template, vm, prestarted_vms, max_user_vms, display, rng_device, soundcard_enabled, type_, use_latest_template_version,  **kwargs_)
supermod.VmPool.subclass = VmPool--super=types
# end class VmPool--super=types


class VmPools--super=types(supermod.VmPools):
    def __init__(self, actions=None, size=None, total=None, active=None, vmpool=None, **kwargs_):
        super(VmPools--super=types, self).__init__(actions, size, total, active, vmpool,  **kwargs_)
supermod.VmPools.subclass = VmPools--super=types
# end class VmPools--super=types


class BaseDevice--super=types(supermod.BaseDevice):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, extensiontype_=None, **kwargs_):
        super(BaseDevice--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, extensiontype_,  **kwargs_)
supermod.BaseDevice.subclass = BaseDevice--super=types
# end class BaseDevice--super=types


class BaseDevices--super=types(supermod.BaseDevices):
    def __init__(self, actions=None, size=None, total=None, active=None, extensiontype_=None, **kwargs_):
        super(BaseDevices--super=types, self).__init__(actions, size, total, active, extensiontype_,  **kwargs_)
supermod.BaseDevices.subclass = BaseDevices--super=types
# end class BaseDevices--super=types


class Application--super=types(supermod.Application):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, vm=None, **kwargs_):
        super(Application--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, vm,  **kwargs_)
supermod.Application.subclass = Application--super=types
# end class Application--super=types


class Applications--super=types(supermod.Applications):
    def __init__(self, actions=None, size=None, total=None, active=None, application=None, **kwargs_):
        super(Applications--super=types, self).__init__(actions, size, total, active, application,  **kwargs_)
supermod.Applications.subclass = Applications--super=types
# end class Applications--super=types


class CdRom--super=types(supermod.CdRom):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, file=None, **kwargs_):
        super(CdRom--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, file,  **kwargs_)
supermod.CdRom.subclass = CdRom--super=types
# end class CdRom--super=types


class CdRoms--super=types(supermod.CdRoms):
    def __init__(self, actions=None, size=None, total=None, active=None, cdrom=None, **kwargs_):
        super(CdRoms--super=types, self).__init__(actions, size, total, active, cdrom,  **kwargs_)
supermod.CdRoms.subclass = CdRoms--super=types
# end class CdRoms--super=types


class Floppy--super=types(supermod.Floppy):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, file=None, **kwargs_):
        super(Floppy--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, file,  **kwargs_)
supermod.Floppy.subclass = Floppy--super=types
# end class Floppy--super=types


class Floppies--super=types(supermod.Floppies):
    def __init__(self, actions=None, size=None, total=None, active=None, floppy=None, **kwargs_):
        super(Floppies--super=types, self).__init__(actions, size, total, active, floppy,  **kwargs_)
supermod.Floppies.subclass = Floppies--super=types
# end class Floppies--super=types


class Disk--super=types(supermod.Disk):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, alias=None, image_id=None, storage_domain=None, storage_domains=None, size=None, type_=None, provisioned_size=None, actual_size=None, status=None, interface=None, format=None, sparse=None, bootable=None, shareable=None, wipe_after_delete=None, propagate_errors=None, statistics=None, active=None, read_only=None, quota=None, lun_storage=None, sgio=None, uses_scsi_reservation=None, snapshot=None, disk_profile=None, logical_name=None, storage_type=None, openstack_volume_type=None, extensiontype_=None, **kwargs_):
        super(Disk--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, alias, image_id, storage_domain, storage_domains, size, type_, provisioned_size, actual_size, status, interface, format, sparse, bootable, shareable, wipe_after_delete, propagate_errors, statistics, active, read_only, quota, lun_storage, sgio, uses_scsi_reservation, snapshot, disk_profile, logical_name, storage_type, openstack_volume_type, extensiontype_,  **kwargs_)
supermod.Disk.subclass = Disk--super=types
# end class Disk--super=types


class Disks--super=types(supermod.Disks):
    def __init__(self, actions=None, size=None, total=None, active=None, disk=None, clone=None, detach_only=None, **kwargs_):
        super(Disks--super=types, self).__init__(actions, size, total, active, disk, clone, detach_only,  **kwargs_)
supermod.Disks.subclass = Disks--super=types
# end class Disks--super=types


class DiskSnapshot--super=types(supermod.DiskSnapshot):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, alias=None, image_id=None, storage_domain=None, storage_domains=None, size=None, type_=None, provisioned_size=None, actual_size=None, status=None, interface=None, format=None, sparse=None, bootable=None, shareable=None, wipe_after_delete=None, propagate_errors=None, statistics=None, active=None, read_only=None, quota=None, lun_storage=None, sgio=None, uses_scsi_reservation=None, snapshot=None, disk_profile=None, logical_name=None, storage_type=None, openstack_volume_type=None, disk=None, **kwargs_):
        super(DiskSnapshot--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, alias, image_id, storage_domain, storage_domains, size, type_, provisioned_size, actual_size, status, interface, format, sparse, bootable, shareable, wipe_after_delete, propagate_errors, statistics, active, read_only, quota, lun_storage, sgio, uses_scsi_reservation, snapshot, disk_profile, logical_name, storage_type, openstack_volume_type, disk,  **kwargs_)
supermod.DiskSnapshot.subclass = DiskSnapshot--super=types
# end class DiskSnapshot--super=types


class DiskSnapshots--super=types(supermod.DiskSnapshots):
    def __init__(self, actions=None, size=None, total=None, active=None, disk_snapshot=None, **kwargs_):
        super(DiskSnapshots--super=types, self).__init__(actions, size, total, active, disk_snapshot,  **kwargs_)
supermod.DiskSnapshots.subclass = DiskSnapshots--super=types
# end class DiskSnapshots--super=types


class DiskStates--super=types(supermod.DiskStates):
    def __init__(self, disk_state=None, **kwargs_):
        super(DiskStates--super=types, self).__init__(disk_state,  **kwargs_)
supermod.DiskStates.subclass = DiskStates--super=types
# end class DiskStates--super=types


class PortMirroring--super=types(supermod.PortMirroring):
    def __init__(self, networks=None, **kwargs_):
        super(PortMirroring--super=types, self).__init__(networks,  **kwargs_)
supermod.PortMirroring.subclass = PortMirroring--super=types
# end class PortMirroring--super=types


class NIC--super=types(supermod.NIC):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, network=None, linked=None, interface=None, mac=None, statistics=None, active=None, plugged=None, port_mirroring=None, reported_devices=None, vnic_profile=None, boot_protocol=None, on_boot=None, **kwargs_):
        super(NIC--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, network, linked, interface, mac, statistics, active, plugged, port_mirroring, reported_devices, vnic_profile, boot_protocol, on_boot,  **kwargs_)
supermod.NIC.subclass = NIC--super=types
# end class NIC--super=types


class Nics--super=types(supermod.Nics):
    def __init__(self, actions=None, size=None, total=None, active=None, nic=None, **kwargs_):
        super(Nics--super=types, self).__init__(actions, size, total, active, nic,  **kwargs_)
supermod.Nics.subclass = Nics--super=types
# end class Nics--super=types


class Snapshot--super=types(supermod.Snapshot):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, status=None, memory=None, cpu=None, cpu_shares=None, bios=None, os=None, cluster=None, storage_domain=None, creation_time=None, origin=None, stateless=None, delete_protected=None, high_availability=None, display=None, sso=None, rng_device=None, console=None, timezone=None, domain=None, usb=None, soundcard_enabled=None, tunnel_migration=None, migration_downtime=None, virtio_scsi=None, serial_number=None, start_paused=None, cpu_profile=None, migration=None, io=None, custom_properties=None, custom_emulated_machine=None, custom_cpu_model=None, time_zone=None, small_icon=None, large_icon=None, memory_policy=None, stop_reason=None, host=None, template=None, instance_type=None, start_time=None, stop_time=None, run_once=None, payloads=None, statistics=None, disks=None, initialization=None, nics=None, tags=None, snapshots=None, placement_policy=None, guest_info=None, quota=None, vmpool=None, cdroms=None, floppies=None, reported_devices=None, watchdogs=None, use_latest_template_version=None, next_run_configuration_exists=None, numa_tune_mode=None, permissions=None, external_host_provider=None, katello_errata=None, guest_time_zone=None, guest_operating_system=None, vm=None, date=None, snapshot_status=None, persist_memorystate=None, **kwargs_):
        super(Snapshot--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, status, memory, cpu, cpu_shares, bios, os, cluster, storage_domain, creation_time, origin, stateless, delete_protected, high_availability, display, sso, rng_device, console, timezone, domain, usb, soundcard_enabled, tunnel_migration, migration_downtime, virtio_scsi, serial_number, start_paused, cpu_profile, migration, io, custom_properties, custom_emulated_machine, custom_cpu_model, time_zone, small_icon, large_icon, memory_policy, stop_reason, host, template, instance_type, start_time, stop_time, run_once, payloads, statistics, disks, initialization, nics, tags, snapshots, placement_policy, guest_info, quota, vmpool, cdroms, floppies, reported_devices, watchdogs, use_latest_template_version, next_run_configuration_exists, numa_tune_mode, permissions, external_host_provider, katello_errata, guest_time_zone, guest_operating_system, vm, date, snapshot_status, persist_memorystate,  **kwargs_)
supermod.Snapshot.subclass = Snapshot--super=types
# end class Snapshot--super=types


class Snapshots--super=types(supermod.Snapshots):
    def __init__(self, actions=None, size=None, total=None, active=None, snapshot=None, collapse_snapshots=None, **kwargs_):
        super(Snapshots--super=types, self).__init__(actions, size, total, active, snapshot, collapse_snapshots,  **kwargs_)
supermod.Snapshots.subclass = Snapshots--super=types
# end class Snapshots--super=types


class HostNIC--super=types(supermod.HostNIC):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, network=None, mac=None, ip=None, base_interface=None, vlan=None, bonding=None, boot_protocol=None, statistics=None, check_connectivity=None, speed=None, status=None, mtu=None, bridged=None, custom_configuration=None, override_configuration=None, labels=None, properties=None, virtual_functions_configuration=None, qos=None, physical_function=None, **kwargs_):
        super(HostNIC--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, network, mac, ip, base_interface, vlan, bonding, boot_protocol, statistics, check_connectivity, speed, status, mtu, bridged, custom_configuration, override_configuration, labels, properties, virtual_functions_configuration, qos, physical_function,  **kwargs_)
supermod.HostNIC.subclass = HostNIC--super=types
# end class HostNIC--super=types


class HostNicVirtualFunctionsConfiguration--super=types(supermod.HostNicVirtualFunctionsConfiguration):
    def __init__(self, max_number_of_virtual_functions=None, number_of_virtual_functions=None, all_networks_allowed=None, **kwargs_):
        super(HostNicVirtualFunctionsConfiguration--super=types, self).__init__(max_number_of_virtual_functions, number_of_virtual_functions, all_networks_allowed,  **kwargs_)
supermod.HostNicVirtualFunctionsConfiguration.subclass = HostNicVirtualFunctionsConfiguration--super=types
# end class HostNicVirtualFunctionsConfiguration--super=types


class UnmanagedNetworks--super=types(supermod.UnmanagedNetworks):
    def __init__(self, actions=None, size=None, total=None, active=None, unmanaged_network=None, **kwargs_):
        super(UnmanagedNetworks--super=types, self).__init__(actions, size, total, active, unmanaged_network,  **kwargs_)
supermod.UnmanagedNetworks.subclass = UnmanagedNetworks--super=types
# end class UnmanagedNetworks--super=types


class UnmanagedNetwork--super=types(supermod.UnmanagedNetwork):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host_nic=None, host=None, **kwargs_):
        super(UnmanagedNetwork--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host_nic, host,  **kwargs_)
supermod.UnmanagedNetwork.subclass = UnmanagedNetwork--super=types
# end class UnmanagedNetwork--super=types


class HostNics--super=types(supermod.HostNics):
    def __init__(self, actions=None, size=None, total=None, active=None, host_nic=None, **kwargs_):
        super(HostNics--super=types, self).__init__(actions, size, total, active, host_nic,  **kwargs_)
supermod.HostNics.subclass = HostNics--super=types
# end class HostNics--super=types


class Product--super=types(supermod.Product):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, **kwargs_):
        super(Product--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link,  **kwargs_)
supermod.Product.subclass = Product--super=types
# end class Product--super=types


class Vendor--super=types(supermod.Vendor):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, **kwargs_):
        super(Vendor--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link,  **kwargs_)
supermod.Vendor.subclass = Vendor--super=types
# end class Vendor--super=types


class HostDevice--super=types(supermod.HostDevice):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, parent_device=None, capability=None, product=None, vendor=None, iommu_group=None, physical_function=None, virtual_functions=None, placeholder=None, vm=None, **kwargs_):
        super(HostDevice--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, parent_device, capability, product, vendor, iommu_group, physical_function, virtual_functions, placeholder, vm,  **kwargs_)
supermod.HostDevice.subclass = HostDevice--super=types
# end class HostDevice--super=types


class HostDevices--super=types(supermod.HostDevices):
    def __init__(self, actions=None, size=None, total=None, active=None, host_device=None, **kwargs_):
        super(HostDevices--super=types, self).__init__(actions, size, total, active, host_device,  **kwargs_)
supermod.HostDevices.subclass = HostDevices--super=types
# end class HostDevices--super=types


class GuestNicConfiguration--super=types(supermod.GuestNicConfiguration):
    def __init__(self, name=None, ip=None, boot_protocol=None, on_boot=None, **kwargs_):
        super(GuestNicConfiguration--super=types, self).__init__(name, ip, boot_protocol, on_boot,  **kwargs_)
supermod.GuestNicConfiguration.subclass = GuestNicConfiguration--super=types
# end class GuestNicConfiguration--super=types


class GuestNicsConfiguration--super=types(supermod.GuestNicsConfiguration):
    def __init__(self, nic_configuration=None, **kwargs_):
        super(GuestNicsConfiguration--super=types, self).__init__(nic_configuration,  **kwargs_)
supermod.GuestNicsConfiguration.subclass = GuestNicsConfiguration--super=types
# end class GuestNicsConfiguration--super=types


class HostNICStates--super=types(supermod.HostNICStates):
    def __init__(self, host_nic_state=None, **kwargs_):
        super(HostNICStates--super=types, self).__init__(host_nic_state,  **kwargs_)
supermod.HostNICStates.subclass = HostNICStates--super=types
# end class HostNICStates--super=types


class Slaves--super=types(supermod.Slaves):
    def __init__(self, host_nic=None, **kwargs_):
        super(Slaves--super=types, self).__init__(host_nic,  **kwargs_)
supermod.Slaves.subclass = Slaves--super=types
# end class Slaves--super=types


class Bonding--super=types(supermod.Bonding):
    def __init__(self, options=None, slaves=None, **kwargs_):
        super(Bonding--super=types, self).__init__(options, slaves,  **kwargs_)
supermod.Bonding.subclass = Bonding--super=types
# end class Bonding--super=types


class NetworkAttachment--super=types(supermod.NetworkAttachment):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, network=None, host_nic=None, ip_address_assignments=None, properties=None, reported_configurations=None, host=None, qos=None, **kwargs_):
        super(NetworkAttachment--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, network, host_nic, ip_address_assignments, properties, reported_configurations, host, qos,  **kwargs_)
supermod.NetworkAttachment.subclass = NetworkAttachment--super=types
# end class NetworkAttachment--super=types


class NetworkAttachments--super=types(supermod.NetworkAttachments):
    def __init__(self, actions=None, size=None, total=None, active=None, network_attachment=None, **kwargs_):
        super(NetworkAttachments--super=types, self).__init__(actions, size, total, active, network_attachment,  **kwargs_)
supermod.NetworkAttachments.subclass = NetworkAttachments--super=types
# end class NetworkAttachments--super=types


class ReportedConfigurations--super=types(supermod.ReportedConfigurations):
    def __init__(self, in_sync=None, reported_configuration=None, **kwargs_):
        super(ReportedConfigurations--super=types, self).__init__(in_sync, reported_configuration,  **kwargs_)
supermod.ReportedConfigurations.subclass = ReportedConfigurations--super=types
# end class ReportedConfigurations--super=types


class ReportedConfiguration--super=types(supermod.ReportedConfiguration):
    def __init__(self, name=None, expected_value=None, actual_value=None, in_sync=None, **kwargs_):
        super(ReportedConfiguration--super=types, self).__init__(name, expected_value, actual_value, in_sync,  **kwargs_)
supermod.ReportedConfiguration.subclass = ReportedConfiguration--super=types
# end class ReportedConfiguration--super=types


class IpAddressAssignments--super=types(supermod.IpAddressAssignments):
    def __init__(self, ip_address_assignment=None, **kwargs_):
        super(IpAddressAssignments--super=types, self).__init__(ip_address_assignment,  **kwargs_)
supermod.IpAddressAssignments.subclass = IpAddressAssignments--super=types
# end class IpAddressAssignments--super=types


class IpAddressAssignment--super=types(supermod.IpAddressAssignment):
    def __init__(self, ip=None, assignment_method=None, **kwargs_):
        super(IpAddressAssignment--super=types, self).__init__(ip, assignment_method,  **kwargs_)
supermod.IpAddressAssignment.subclass = IpAddressAssignment--super=types
# end class IpAddressAssignment--super=types


class HostStorage--super=types(supermod.HostStorage):
    def __init__(self, actions=None, size=None, total=None, active=None, storage=None, **kwargs_):
        super(HostStorage--super=types, self).__init__(actions, size, total, active, storage,  **kwargs_)
supermod.HostStorage.subclass = HostStorage--super=types
# end class HostStorage--super=types


class Bookmark--super=types(supermod.Bookmark):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, value=None, **kwargs_):
        super(Bookmark--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, value,  **kwargs_)
supermod.Bookmark.subclass = Bookmark--super=types
# end class Bookmark--super=types


class Bookmarks--super=types(supermod.Bookmarks):
    def __init__(self, actions=None, size=None, total=None, active=None, bookmark=None, **kwargs_):
        super(Bookmarks--super=types, self).__init__(actions, size, total, active, bookmark,  **kwargs_)
supermod.Bookmarks.subclass = Bookmarks--super=types
# end class Bookmarks--super=types


class TagParent--super=types(supermod.TagParent):
    def __init__(self, tag=None, **kwargs_):
        super(TagParent--super=types, self).__init__(tag,  **kwargs_)
supermod.TagParent.subclass = TagParent--super=types
# end class TagParent--super=types


class Tag--super=types(supermod.Tag):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, vm=None, template=None, user=None, group=None, parent=None, **kwargs_):
        super(Tag--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, vm, template, user, group, parent,  **kwargs_)
supermod.Tag.subclass = Tag--super=types
# end class Tag--super=types


class Tags--super=types(supermod.Tags):
    def __init__(self, actions=None, size=None, total=None, active=None, tag=None, **kwargs_):
        super(Tags--super=types, self).__init__(actions, size, total, active, tag,  **kwargs_)
supermod.Tags.subclass = Tags--super=types
# end class Tags--super=types


class Usb--super=types(supermod.Usb):
    def __init__(self, enabled=None, type_=None, **kwargs_):
        super(Usb--super=types, self).__init__(enabled, type_,  **kwargs_)
supermod.Usb.subclass = Usb--super=types
# end class Usb--super=types


class Quota--super=types(supermod.Quota):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, data_center=None, vms=None, disks=None, users=None, cluster_soft_limit_pct=None, cluster_hard_limit_pct=None, storage_soft_limit_pct=None, storage_hard_limit_pct=None, **kwargs_):
        super(Quota--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, data_center, vms, disks, users, cluster_soft_limit_pct, cluster_hard_limit_pct, storage_soft_limit_pct, storage_hard_limit_pct,  **kwargs_)
supermod.Quota.subclass = Quota--super=types
# end class Quota--super=types


class Quotas--super=types(supermod.Quotas):
    def __init__(self, actions=None, size=None, total=None, active=None, quota=None, **kwargs_):
        super(Quotas--super=types, self).__init__(actions, size, total, active, quota,  **kwargs_)
supermod.Quotas.subclass = Quotas--super=types
# end class Quotas--super=types


class QuotaStorageLimit--super=types(supermod.QuotaStorageLimit):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, quota=None, storage_domain=None, limit=None, usage=None, **kwargs_):
        super(QuotaStorageLimit--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, quota, storage_domain, limit, usage,  **kwargs_)
supermod.QuotaStorageLimit.subclass = QuotaStorageLimit--super=types
# end class QuotaStorageLimit--super=types


class QuotaStorageLimits--super=types(supermod.QuotaStorageLimits):
    def __init__(self, actions=None, size=None, total=None, active=None, storage_quota_limit=None, **kwargs_):
        super(QuotaStorageLimits--super=types, self).__init__(actions, size, total, active, storage_quota_limit,  **kwargs_)
supermod.QuotaStorageLimits.subclass = QuotaStorageLimits--super=types
# end class QuotaStorageLimits--super=types


class QuotaClusterLimit--super=types(supermod.QuotaClusterLimit):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, quota=None, cluster=None, vcpu_limit=None, vcpu_usage=None, memory_limit=None, memory_usage=None, **kwargs_):
        super(QuotaClusterLimit--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, quota, cluster, vcpu_limit, vcpu_usage, memory_limit, memory_usage,  **kwargs_)
supermod.QuotaClusterLimit.subclass = QuotaClusterLimit--super=types
# end class QuotaClusterLimit--super=types


class QuotaClusterLimits--super=types(supermod.QuotaClusterLimits):
    def __init__(self, actions=None, size=None, total=None, active=None, cluster_quota_limit=None, **kwargs_):
        super(QuotaClusterLimits--super=types, self).__init__(actions, size, total, active, cluster_quota_limit,  **kwargs_)
supermod.QuotaClusterLimits.subclass = QuotaClusterLimits--super=types
# end class QuotaClusterLimits--super=types


class Url--super=types(supermod.Url):
    def __init__(self, parameters_set=None, **kwargs_):
        super(Url--super=types, self).__init__(parameters_set,  **kwargs_)
supermod.Url.subclass = Url--super=types
# end class Url--super=types


class Body--super=types(supermod.Body):
    def __init__(self, required=None, type_=None, parameters_set=None, **kwargs_):
        super(Body--super=types, self).__init__(required, type_, parameters_set,  **kwargs_)
supermod.Body.subclass = Body--super=types
# end class Body--super=types


class Request--super=types(supermod.Request):
    def __init__(self, http_method=None, headers=None, url=None, body=None, **kwargs_):
        super(Request--super=types, self).__init__(http_method, headers, url, body,  **kwargs_)
supermod.Request.subclass = Request--super=types
# end class Request--super=types


class Response--super=types(supermod.Response):
    def __init__(self, type_=None, **kwargs_):
        super(Response--super=types, self).__init__(type_,  **kwargs_)
supermod.Response.subclass = Response--super=types
# end class Response--super=types


class Parameter--super=types(supermod.Parameter):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, required=None, type_=None, context=None, value=None, parameters_set=None, deprecated=None, **kwargs_):
        super(Parameter--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, required, type_, context, value, parameters_set, deprecated,  **kwargs_)
supermod.Parameter.subclass = Parameter--super=types
# end class Parameter--super=types


class Header--super=types(supermod.Header):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, required=None, value=None, deprecated=None, **kwargs_):
        super(Header--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, required, value, deprecated,  **kwargs_)
supermod.Header.subclass = Header--super=types
# end class Header--super=types


class Headers--super=types(supermod.Headers):
    def __init__(self, header=None, **kwargs_):
        super(Headers--super=types, self).__init__(header,  **kwargs_)
supermod.Headers.subclass = Headers--super=types
# end class Headers--super=types


class ParametersSet--super=types(supermod.ParametersSet):
    def __init__(self, deprecated=None, description=None, parameter=None, **kwargs_):
        super(ParametersSet--super=types, self).__init__(deprecated, description, parameter,  **kwargs_)
supermod.ParametersSet.subclass = ParametersSet--super=types
# end class ParametersSet--super=types


class Schema--super=types(supermod.Schema):
    def __init__(self, href=None, rel=None, name=None, description=None, **kwargs_):
        super(Schema--super=types, self).__init__(href, rel, name, description,  **kwargs_)
supermod.Schema.subclass = Schema--super=types
# end class Schema--super=types


class RSDL--super=types(supermod.RSDL):
    def __init__(self, href=None, rel=None, description=None, version=None, schema=None, general=None, links=None, **kwargs_):
        super(RSDL--super=types, self).__init__(href, rel, description, version, schema, general, links,  **kwargs_)
supermod.RSDL.subclass = RSDL--super=types
# end class RSDL--super=types


class GlusterVolume--super=types(supermod.GlusterVolume):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, cluster=None, volume_type=None, transport_types=None, replica_count=None, stripe_count=None, disperse_count=None, redundancy_count=None, bricks=None, options=None, status=None, **kwargs_):
        super(GlusterVolume--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, cluster, volume_type, transport_types, replica_count, stripe_count, disperse_count, redundancy_count, bricks, options, status,  **kwargs_)
supermod.GlusterVolume.subclass = GlusterVolume--super=types
# end class GlusterVolume--super=types


class GlusterVolumeTypes--super=types(supermod.GlusterVolumeTypes):
    def __init__(self, gluster_volume_type=None, **kwargs_):
        super(GlusterVolumeTypes--super=types, self).__init__(gluster_volume_type,  **kwargs_)
supermod.GlusterVolumeTypes.subclass = GlusterVolumeTypes--super=types
# end class GlusterVolumeTypes--super=types


class TransportTypes--super=types(supermod.TransportTypes):
    def __init__(self, transport_type=None, **kwargs_):
        super(TransportTypes--super=types, self).__init__(transport_type,  **kwargs_)
supermod.TransportTypes.subclass = TransportTypes--super=types
# end class TransportTypes--super=types


class GlusterStates--super=types(supermod.GlusterStates):
    def __init__(self, state=None, **kwargs_):
        super(GlusterStates--super=types, self).__init__(state,  **kwargs_)
supermod.GlusterStates.subclass = GlusterStates--super=types
# end class GlusterStates--super=types


class GlusterVolumes--super=types(supermod.GlusterVolumes):
    def __init__(self, actions=None, size=None, total=None, active=None, gluster_volume=None, **kwargs_):
        super(GlusterVolumes--super=types, self).__init__(actions, size, total, active, gluster_volume,  **kwargs_)
supermod.GlusterVolumes.subclass = GlusterVolumes--super=types
# end class GlusterVolumes--super=types


class GlusterClient--super=types(supermod.GlusterClient):
    def __init__(self, host_name=None, client_port=None, bytes_read=None, bytes_written=None, **kwargs_):
        super(GlusterClient--super=types, self).__init__(host_name, client_port, bytes_read, bytes_written,  **kwargs_)
supermod.GlusterClient.subclass = GlusterClient--super=types
# end class GlusterClient--super=types


class GlusterClients--super=types(supermod.GlusterClients):
    def __init__(self, actions=None, size=None, total=None, active=None, gluster_client=None, **kwargs_):
        super(GlusterClients--super=types, self).__init__(actions, size, total, active, gluster_client,  **kwargs_)
supermod.GlusterClients.subclass = GlusterClients--super=types
# end class GlusterClients--super=types


class GlusterMemoryPool--super=types(supermod.GlusterMemoryPool):
    def __init__(self, name=None, hot_count=None, cold_count=None, padded_size=None, alloc_count=None, max_alloc=None, pool_misses=None, max_stdalloc=None, **kwargs_):
        super(GlusterMemoryPool--super=types, self).__init__(name, hot_count, cold_count, padded_size, alloc_count, max_alloc, pool_misses, max_stdalloc,  **kwargs_)
supermod.GlusterMemoryPool.subclass = GlusterMemoryPool--super=types
# end class GlusterMemoryPool--super=types


class GlusterMemoryPools--super=types(supermod.GlusterMemoryPools):
    def __init__(self, actions=None, size=None, total=None, active=None, memory_pool=None, **kwargs_):
        super(GlusterMemoryPools--super=types, self).__init__(actions, size, total, active, memory_pool,  **kwargs_)
supermod.GlusterMemoryPools.subclass = GlusterMemoryPools--super=types
# end class GlusterMemoryPools--super=types


class GlusterBrickMemoryInfo--super=types(supermod.GlusterBrickMemoryInfo):
    def __init__(self, memory_pools=None, **kwargs_):
        super(GlusterBrickMemoryInfo--super=types, self).__init__(memory_pools,  **kwargs_)
supermod.GlusterBrickMemoryInfo.subclass = GlusterBrickMemoryInfo--super=types
# end class GlusterBrickMemoryInfo--super=types


class GlusterBrickAdvancedDetails--super=types(supermod.GlusterBrickAdvancedDetails):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, port=None, pid=None, device=None, mnt_options=None, fs_name=None, gluster_clients=None, memory_pools=None, extensiontype_=None, **kwargs_):
        super(GlusterBrickAdvancedDetails--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, port, pid, device, mnt_options, fs_name, gluster_clients, memory_pools, extensiontype_,  **kwargs_)
supermod.GlusterBrickAdvancedDetails.subclass = GlusterBrickAdvancedDetails--super=types
# end class GlusterBrickAdvancedDetails--super=types


class GlusterBrick--super=types(supermod.GlusterBrick):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, port=None, pid=None, device=None, mnt_options=None, fs_name=None, gluster_clients=None, memory_pools=None, gluster_volume=None, server_id=None, brick_dir=None, status=None, **kwargs_):
        super(GlusterBrick--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, port, pid, device, mnt_options, fs_name, gluster_clients, memory_pools, gluster_volume, server_id, brick_dir, status,  **kwargs_)
supermod.GlusterBrick.subclass = GlusterBrick--super=types
# end class GlusterBrick--super=types


class GlusterBricks--super=types(supermod.GlusterBricks):
    def __init__(self, actions=None, size=None, total=None, active=None, replica_count=None, stripe_count=None, brick=None, **kwargs_):
        super(GlusterBricks--super=types, self).__init__(actions, size, total, active, replica_count, stripe_count, brick,  **kwargs_)
supermod.GlusterBricks.subclass = GlusterBricks--super=types
# end class GlusterBricks--super=types


class Stages--super=types(supermod.Stages):
    def __init__(self, stage=None, **kwargs_):
        super(Stages--super=types, self).__init__(stage,  **kwargs_)
supermod.Stages.subclass = Stages--super=types
# end class Stages--super=types


class HookStates--super=types(supermod.HookStates):
    def __init__(self, hook_state=None, **kwargs_):
        super(HookStates--super=types, self).__init__(hook_state,  **kwargs_)
supermod.HookStates.subclass = HookStates--super=types
# end class HookStates--super=types


class ContentTypes--super=types(supermod.ContentTypes):
    def __init__(self, content_type=None, **kwargs_):
        super(ContentTypes--super=types, self).__init__(content_type,  **kwargs_)
supermod.ContentTypes.subclass = ContentTypes--super=types
# end class ContentTypes--super=types


class GlusterServerHooks--super=types(supermod.GlusterServerHooks):
    def __init__(self, actions=None, size=None, total=None, active=None, server_hook=None, **kwargs_):
        super(GlusterServerHooks--super=types, self).__init__(actions, size, total, active, server_hook,  **kwargs_)
supermod.GlusterServerHooks.subclass = GlusterServerHooks--super=types
# end class GlusterServerHooks--super=types


class GlusterServerHook--super=types(supermod.GlusterServerHook):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, content_type=None, status=None, checksum=None, **kwargs_):
        super(GlusterServerHook--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, content_type, status, checksum,  **kwargs_)
supermod.GlusterServerHook.subclass = GlusterServerHook--super=types
# end class GlusterServerHook--super=types


class GlusterHook--super=types(supermod.GlusterHook):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, cluster=None, gluster_command=None, stage=None, content_type=None, checksum=None, content=None, conflict_status=None, conflicts=None, status=None, server_hooks=None, **kwargs_):
        super(GlusterHook--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, cluster, gluster_command, stage, content_type, checksum, content, conflict_status, conflicts, status, server_hooks,  **kwargs_)
supermod.GlusterHook.subclass = GlusterHook--super=types
# end class GlusterHook--super=types


class GlusterHooks--super=types(supermod.GlusterHooks):
    def __init__(self, actions=None, size=None, total=None, active=None, gluster_hook=None, **kwargs_):
        super(GlusterHooks--super=types, self).__init__(actions, size, total, active, gluster_hook,  **kwargs_)
supermod.GlusterHooks.subclass = GlusterHooks--super=types
# end class GlusterHooks--super=types


class GlusterVolumeProfileDetails--super=types(supermod.GlusterVolumeProfileDetails):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, brick_profile_details=None, nfs_profile_details=None, **kwargs_):
        super(GlusterVolumeProfileDetails--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, brick_profile_details, nfs_profile_details,  **kwargs_)
supermod.GlusterVolumeProfileDetails.subclass = GlusterVolumeProfileDetails--super=types
# end class GlusterVolumeProfileDetails--super=types


class BrickProfileDetails--super=types(supermod.BrickProfileDetails):
    def __init__(self, brick_profile_detail=None, **kwargs_):
        super(BrickProfileDetails--super=types, self).__init__(brick_profile_detail,  **kwargs_)
supermod.BrickProfileDetails.subclass = BrickProfileDetails--super=types
# end class BrickProfileDetails--super=types


class NfsProfileDetails--super=types(supermod.NfsProfileDetails):
    def __init__(self, nfs_profile_detail=None, **kwargs_):
        super(NfsProfileDetails--super=types, self).__init__(nfs_profile_detail,  **kwargs_)
supermod.NfsProfileDetails.subclass = NfsProfileDetails--super=types
# end class NfsProfileDetails--super=types


class EntityProfileDetail--super=types(supermod.EntityProfileDetail):
    def __init__(self, profile_detail=None, extensiontype_=None, **kwargs_):
        super(EntityProfileDetail--super=types, self).__init__(profile_detail, extensiontype_,  **kwargs_)
supermod.EntityProfileDetail.subclass = EntityProfileDetail--super=types
# end class EntityProfileDetail--super=types


class NfsProfileDetail--super=types(supermod.NfsProfileDetail):
    def __init__(self, profile_detail=None, nfs_server_ip=None, **kwargs_):
        super(NfsProfileDetail--super=types, self).__init__(profile_detail, nfs_server_ip,  **kwargs_)
supermod.NfsProfileDetail.subclass = NfsProfileDetail--super=types
# end class NfsProfileDetail--super=types


class ProfileDetail--super=types(supermod.ProfileDetail):
    def __init__(self, profile_type=None, duration=None, statistic=None, block_statistic=None, fop_statistic=None, **kwargs_):
        super(ProfileDetail--super=types, self).__init__(profile_type, duration, statistic, block_statistic, fop_statistic,  **kwargs_)
supermod.ProfileDetail.subclass = ProfileDetail--super=types
# end class ProfileDetail--super=types


class BlockStatistic--super=types(supermod.BlockStatistic):
    def __init__(self, statistic=None, **kwargs_):
        super(BlockStatistic--super=types, self).__init__(statistic,  **kwargs_)
supermod.BlockStatistic.subclass = BlockStatistic--super=types
# end class BlockStatistic--super=types


class FopStatistic--super=types(supermod.FopStatistic):
    def __init__(self, name=None, statistic=None, **kwargs_):
        super(FopStatistic--super=types, self).__init__(name, statistic,  **kwargs_)
supermod.FopStatistic.subclass = FopStatistic--super=types
# end class FopStatistic--super=types


class PmProxies--super=types(supermod.PmProxies):
    def __init__(self, pm_proxy=None, **kwargs_):
        super(PmProxies--super=types, self).__init__(pm_proxy,  **kwargs_)
supermod.PmProxies.subclass = PmProxies--super=types
# end class PmProxies--super=types


class PmProxy--super=types(supermod.PmProxy):
    def __init__(self, type_=None, **kwargs_):
        super(PmProxy--super=types, self).__init__(type_,  **kwargs_)
supermod.PmProxy.subclass = PmProxy--super=types
# end class PmProxy--super=types


class StepTypes--super=types(supermod.StepTypes):
    def __init__(self, step_type=None, **kwargs_):
        super(StepTypes--super=types, self).__init__(step_type,  **kwargs_)
supermod.StepTypes.subclass = StepTypes--super=types
# end class StepTypes--super=types


class Step--super=types(supermod.Step):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, parent_step=None, job=None, type_=None, number=None, status=None, start_time=None, end_time=None, external=None, external_type=None, **kwargs_):
        super(Step--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, parent_step, job, type_, number, status, start_time, end_time, external, external_type,  **kwargs_)
supermod.Step.subclass = Step--super=types
# end class Step--super=types


class Steps--super=types(supermod.Steps):
    def __init__(self, actions=None, size=None, total=None, active=None, step=None, **kwargs_):
        super(Steps--super=types, self).__init__(actions, size, total, active, step,  **kwargs_)
supermod.Steps.subclass = Steps--super=types
# end class Steps--super=types


class Job--super=types(supermod.Job):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, status=None, owner=None, start_time=None, end_time=None, last_updated=None, external=None, auto_cleared=None, **kwargs_):
        super(Job--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, status, owner, start_time, end_time, last_updated, external, auto_cleared,  **kwargs_)
supermod.Job.subclass = Job--super=types
# end class Job--super=types


class Jobs--super=types(supermod.Jobs):
    def __init__(self, actions=None, size=None, total=None, active=None, job=None, **kwargs_):
        super(Jobs--super=types, self).__init__(actions, size, total, active, job,  **kwargs_)
supermod.Jobs.subclass = Jobs--super=types
# end class Jobs--super=types


class AffinityGroup--super=types(supermod.AffinityGroup):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, cluster=None, positive=None, enforcing=None, **kwargs_):
        super(AffinityGroup--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, cluster, positive, enforcing,  **kwargs_)
supermod.AffinityGroup.subclass = AffinityGroup--super=types
# end class AffinityGroup--super=types


class AffinityGroups--super=types(supermod.AffinityGroups):
    def __init__(self, actions=None, size=None, total=None, active=None, affinity_group=None, **kwargs_):
        super(AffinityGroups--super=types, self).__init__(actions, size, total, active, affinity_group,  **kwargs_)
supermod.AffinityGroups.subclass = AffinityGroups--super=types
# end class AffinityGroups--super=types


class NumaNode--super=types(supermod.NumaNode):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, index=None, memory=None, cpu=None, statistics=None, node_distance=None, extensiontype_=None, **kwargs_):
        super(NumaNode--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, index, memory, cpu, statistics, node_distance, extensiontype_,  **kwargs_)
supermod.NumaNode.subclass = NumaNode--super=types
# end class NumaNode--super=types


class QoS--super=types(supermod.QoS):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, data_center=None, max_throughput=None, max_read_throughput=None, max_write_throughput=None, max_iops=None, max_read_iops=None, max_write_iops=None, cpu_limit=None, inbound_average=None, inbound_peak=None, inbound_burst=None, outbound_average=None, outbound_peak=None, outbound_burst=None, outbound_average_linkshare=None, outbound_average_upperlimit=None, outbound_average_realtime=None, **kwargs_):
        super(QoS--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, data_center, max_throughput, max_read_throughput, max_write_throughput, max_iops, max_read_iops, max_write_iops, cpu_limit, inbound_average, inbound_peak, inbound_burst, outbound_average, outbound_peak, outbound_burst, outbound_average_linkshare, outbound_average_upperlimit, outbound_average_realtime,  **kwargs_)
supermod.QoS.subclass = QoS--super=types
# end class QoS--super=types


class NumaNodes--super=types(supermod.NumaNodes):
    def __init__(self, actions=None, size=None, total=None, active=None, host_numa_node=None, extensiontype_=None, **kwargs_):
        super(NumaNodes--super=types, self).__init__(actions, size, total, active, host_numa_node, extensiontype_,  **kwargs_)
supermod.NumaNodes.subclass = NumaNodes--super=types
# end class NumaNodes--super=types


class VirtualNumaNode--super=types(supermod.VirtualNumaNode):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, host=None, index=None, memory=None, cpu=None, statistics=None, node_distance=None, vm=None, numa_node_pins=None, **kwargs_):
        super(VirtualNumaNode--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, host, index, memory, cpu, statistics, node_distance, vm, numa_node_pins,  **kwargs_)
supermod.VirtualNumaNode.subclass = VirtualNumaNode--super=types
# end class VirtualNumaNode--super=types


class VirtualNumaNodes--super=types(supermod.VirtualNumaNodes):
    def __init__(self, actions=None, size=None, total=None, active=None, host_numa_node=None, vm_numa_node=None, **kwargs_):
        super(VirtualNumaNodes--super=types, self).__init__(actions, size, total, active, host_numa_node, vm_numa_node,  **kwargs_)
supermod.VirtualNumaNodes.subclass = VirtualNumaNodes--super=types
# end class VirtualNumaNodes--super=types


class QoSs--super=types(supermod.QoSs):
    def __init__(self, actions=None, size=None, total=None, active=None, qos=None, **kwargs_):
        super(QoSs--super=types, self).__init__(actions, size, total, active, qos,  **kwargs_)
supermod.QoSs.subclass = QoSs--super=types
# end class QoSs--super=types


class NumaNodePins--super=types(supermod.NumaNodePins):
    def __init__(self, numa_node_pin=None, **kwargs_):
        super(NumaNodePins--super=types, self).__init__(numa_node_pin,  **kwargs_)
supermod.NumaNodePins.subclass = NumaNodePins--super=types
# end class NumaNodePins--super=types


class NumaNodePin--super=types(supermod.NumaNodePin):
    def __init__(self, pinned=None, index=None, host_numa_node=None, **kwargs_):
        super(NumaNodePin--super=types, self).__init__(pinned, index, host_numa_node,  **kwargs_)
supermod.NumaNodePin.subclass = NumaNodePin--super=types
# end class NumaNodePin--super=types


class Cores--super=types(supermod.Cores):
    def __init__(self, core=None, **kwargs_):
        super(Cores--super=types, self).__init__(core,  **kwargs_)
supermod.Cores.subclass = Cores--super=types
# end class Cores--super=types


class Core--super=types(supermod.Core):
    def __init__(self, index=None, socket=None, **kwargs_):
        super(Core--super=types, self).__init__(index, socket,  **kwargs_)
supermod.Core.subclass = Core--super=types
# end class Core--super=types


class QosTypes--super=types(supermod.QosTypes):
    def __init__(self, qos_type=None, **kwargs_):
        super(QosTypes--super=types, self).__init__(qos_type,  **kwargs_)
supermod.QosTypes.subclass = QosTypes--super=types
# end class QosTypes--super=types


class IscsiBond--super=types(supermod.IscsiBond):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, data_center=None, storage_connections=None, networks=None, **kwargs_):
        super(IscsiBond--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, data_center, storage_connections, networks,  **kwargs_)
supermod.IscsiBond.subclass = IscsiBond--super=types
# end class IscsiBond--super=types


class IscsiBonds--super=types(supermod.IscsiBonds):
    def __init__(self, actions=None, size=None, total=None, active=None, iscsi_bond=None, **kwargs_):
        super(IscsiBonds--super=types, self).__init__(actions, size, total, active, iscsi_bond,  **kwargs_)
supermod.IscsiBonds.subclass = IscsiBonds--super=types
# end class IscsiBonds--super=types


class DiskProfile--super=types(supermod.DiskProfile):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, qos=None, storage_domain=None, **kwargs_):
        super(DiskProfile--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, qos, storage_domain,  **kwargs_)
supermod.DiskProfile.subclass = DiskProfile--super=types
# end class DiskProfile--super=types


class DiskProfiles--super=types(supermod.DiskProfiles):
    def __init__(self, actions=None, size=None, total=None, active=None, disk_profile=None, **kwargs_):
        super(DiskProfiles--super=types, self).__init__(actions, size, total, active, disk_profile,  **kwargs_)
supermod.DiskProfiles.subclass = DiskProfiles--super=types
# end class DiskProfiles--super=types


class CpuProfile--super=types(supermod.CpuProfile):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, qos=None, cluster=None, **kwargs_):
        super(CpuProfile--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, qos, cluster,  **kwargs_)
supermod.CpuProfile.subclass = CpuProfile--super=types
# end class CpuProfile--super=types


class CpuProfiles--super=types(supermod.CpuProfiles):
    def __init__(self, actions=None, size=None, total=None, active=None, cpu_profile=None, **kwargs_):
        super(CpuProfiles--super=types, self).__init__(actions, size, total, active, cpu_profile,  **kwargs_)
supermod.CpuProfiles.subclass = CpuProfiles--super=types
# end class CpuProfiles--super=types


class OperatingSystemInfo--super=types(supermod.OperatingSystemInfo):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, large_icon=None, small_icon=None, **kwargs_):
        super(OperatingSystemInfo--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, large_icon, small_icon,  **kwargs_)
supermod.OperatingSystemInfo.subclass = OperatingSystemInfo--super=types
# end class OperatingSystemInfo--super=types


class OperatingSystemInfos--super=types(supermod.OperatingSystemInfos):
    def __init__(self, actions=None, size=None, total=None, active=None, operating_system=None, **kwargs_):
        super(OperatingSystemInfos--super=types, self).__init__(actions, size, total, active, operating_system,  **kwargs_)
supermod.OperatingSystemInfos.subclass = OperatingSystemInfos--super=types
# end class OperatingSystemInfos--super=types


class ExternalProvider--super=types(supermod.ExternalProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, extensiontype_=None, **kwargs_):
        super(ExternalProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties, extensiontype_,  **kwargs_)
supermod.ExternalProvider.subclass = ExternalProvider--super=types
# end class ExternalProvider--super=types


class ExternalHostProvider--super=types(supermod.ExternalHostProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, **kwargs_):
        super(ExternalHostProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties,  **kwargs_)
supermod.ExternalHostProvider.subclass = ExternalHostProvider--super=types
# end class ExternalHostProvider--super=types


class ExternalHostProviders--super=types(supermod.ExternalHostProviders):
    def __init__(self, actions=None, size=None, total=None, active=None, external_host_provider=None, **kwargs_):
        super(ExternalHostProviders--super=types, self).__init__(actions, size, total, active, external_host_provider,  **kwargs_)
supermod.ExternalHostProviders.subclass = ExternalHostProviders--super=types
# end class ExternalHostProviders--super=types


class ExternalHost--super=types(supermod.ExternalHost):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, external_host_provider=None, address=None, **kwargs_):
        super(ExternalHost--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, external_host_provider, address,  **kwargs_)
supermod.ExternalHost.subclass = ExternalHost--super=types
# end class ExternalHost--super=types


class ExternalHosts--super=types(supermod.ExternalHosts):
    def __init__(self, actions=None, size=None, total=None, active=None, external_host=None, **kwargs_):
        super(ExternalHosts--super=types, self).__init__(actions, size, total, active, external_host,  **kwargs_)
supermod.ExternalHosts.subclass = ExternalHosts--super=types
# end class ExternalHosts--super=types


class ExternalDiscoveredHost--super=types(supermod.ExternalDiscoveredHost):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, ip=None, mac=None, subnet_name=None, last_report=None, external_host_provider=None, **kwargs_):
        super(ExternalDiscoveredHost--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, ip, mac, subnet_name, last_report, external_host_provider,  **kwargs_)
supermod.ExternalDiscoveredHost.subclass = ExternalDiscoveredHost--super=types
# end class ExternalDiscoveredHost--super=types


class ExternalDiscoveredHosts--super=types(supermod.ExternalDiscoveredHosts):
    def __init__(self, actions=None, size=None, total=None, active=None, external_discovered_host=None, **kwargs_):
        super(ExternalDiscoveredHosts--super=types, self).__init__(actions, size, total, active, external_discovered_host,  **kwargs_)
supermod.ExternalDiscoveredHosts.subclass = ExternalDiscoveredHosts--super=types
# end class ExternalDiscoveredHosts--super=types


class ExternalHostGroup--super=types(supermod.ExternalHostGroup):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, architecture_name=None, operating_system_name=None, domain_name=None, subnet_name=None, external_host_provider=None, **kwargs_):
        super(ExternalHostGroup--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, architecture_name, operating_system_name, domain_name, subnet_name, external_host_provider,  **kwargs_)
supermod.ExternalHostGroup.subclass = ExternalHostGroup--super=types
# end class ExternalHostGroup--super=types


class ExternalHostGroups--super=types(supermod.ExternalHostGroups):
    def __init__(self, actions=None, size=None, total=None, active=None, external_host_group=None, **kwargs_):
        super(ExternalHostGroups--super=types, self).__init__(actions, size, total, active, external_host_group,  **kwargs_)
supermod.ExternalHostGroups.subclass = ExternalHostGroups--super=types
# end class ExternalHostGroups--super=types


class ExternalComputeResource--super=types(supermod.ExternalComputeResource):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, provider=None, user=None, url=None, external_host_provider=None, **kwargs_):
        super(ExternalComputeResource--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, provider, user, url, external_host_provider,  **kwargs_)
supermod.ExternalComputeResource.subclass = ExternalComputeResource--super=types
# end class ExternalComputeResource--super=types


class ExternalComputeResources--super=types(supermod.ExternalComputeResources):
    def __init__(self, actions=None, size=None, total=None, active=None, external_compute_resource=None, **kwargs_):
        super(ExternalComputeResources--super=types, self).__init__(actions, size, total, active, external_compute_resource,  **kwargs_)
supermod.ExternalComputeResources.subclass = ExternalComputeResources--super=types
# end class ExternalComputeResources--super=types


class OpenStackProvider--super=types(supermod.OpenStackProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, tenant_name=None, extensiontype_=None, **kwargs_):
        super(OpenStackProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties, tenant_name, extensiontype_,  **kwargs_)
supermod.OpenStackProvider.subclass = OpenStackProvider--super=types
# end class OpenStackProvider--super=types


class OpenStackImageProvider--super=types(supermod.OpenStackImageProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, tenant_name=None, **kwargs_):
        super(OpenStackImageProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties, tenant_name,  **kwargs_)
supermod.OpenStackImageProvider.subclass = OpenStackImageProvider--super=types
# end class OpenStackImageProvider--super=types


class OpenStackImageProviders--super=types(supermod.OpenStackImageProviders):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_image_provider=None, **kwargs_):
        super(OpenStackImageProviders--super=types, self).__init__(actions, size, total, active, openstack_image_provider,  **kwargs_)
supermod.OpenStackImageProviders.subclass = OpenStackImageProviders--super=types
# end class OpenStackImageProviders--super=types


class OpenStackImage--super=types(supermod.OpenStackImage):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, openstack_image_provider=None, **kwargs_):
        super(OpenStackImage--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, openstack_image_provider,  **kwargs_)
supermod.OpenStackImage.subclass = OpenStackImage--super=types
# end class OpenStackImage--super=types


class OpenStackImages--super=types(supermod.OpenStackImages):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_image=None, **kwargs_):
        super(OpenStackImages--super=types, self).__init__(actions, size, total, active, openstack_image,  **kwargs_)
supermod.OpenStackImages.subclass = OpenStackImages--super=types
# end class OpenStackImages--super=types


class OpenStackVolumeProvider--super=types(supermod.OpenStackVolumeProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, tenant_name=None, data_center=None, **kwargs_):
        super(OpenStackVolumeProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties, tenant_name, data_center,  **kwargs_)
supermod.OpenStackVolumeProvider.subclass = OpenStackVolumeProvider--super=types
# end class OpenStackVolumeProvider--super=types


class OpenStackVolumeProviders--super=types(supermod.OpenStackVolumeProviders):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_volume_provider=None, **kwargs_):
        super(OpenStackVolumeProviders--super=types, self).__init__(actions, size, total, active, openstack_volume_provider,  **kwargs_)
supermod.OpenStackVolumeProviders.subclass = OpenStackVolumeProviders--super=types
# end class OpenStackVolumeProviders--super=types


class OpenStackVolumeType--super=types(supermod.OpenStackVolumeType):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, properties=None, openstack_volume_provider=None, **kwargs_):
        super(OpenStackVolumeType--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, properties, openstack_volume_provider,  **kwargs_)
supermod.OpenStackVolumeType.subclass = OpenStackVolumeType--super=types
# end class OpenStackVolumeType--super=types


class OpenStackVolumeTypes--super=types(supermod.OpenStackVolumeTypes):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_volume_type=None, **kwargs_):
        super(OpenStackVolumeTypes--super=types, self).__init__(actions, size, total, active, openstack_volume_type,  **kwargs_)
supermod.OpenStackVolumeTypes.subclass = OpenStackVolumeTypes--super=types
# end class OpenStackVolumeTypes--super=types


class OpenstackVolumeAuthenticationKey--super=types(supermod.OpenstackVolumeAuthenticationKey):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, uuid=None, value=None, usage_type=None, creation_date=None, openstack_volume_provider=None, **kwargs_):
        super(OpenstackVolumeAuthenticationKey--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, uuid, value, usage_type, creation_date, openstack_volume_provider,  **kwargs_)
supermod.OpenstackVolumeAuthenticationKey.subclass = OpenstackVolumeAuthenticationKey--super=types
# end class OpenstackVolumeAuthenticationKey--super=types


class OpenstackVolumeAuthenticationKeys--super=types(supermod.OpenstackVolumeAuthenticationKeys):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_volume_authentication_key=None, **kwargs_):
        super(OpenstackVolumeAuthenticationKeys--super=types, self).__init__(actions, size, total, active, openstack_volume_authentication_key,  **kwargs_)
supermod.OpenstackVolumeAuthenticationKeys.subclass = OpenstackVolumeAuthenticationKeys--super=types
# end class OpenstackVolumeAuthenticationKeys--super=types


class OpenStackNetworkProvider--super=types(supermod.OpenStackNetworkProvider):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, url=None, requires_authentication=None, username=None, password=None, authentication_url=None, properties=None, tenant_name=None, plugin_type=None, agent_configuration=None, **kwargs_):
        super(OpenStackNetworkProvider--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, url, requires_authentication, username, password, authentication_url, properties, tenant_name, plugin_type, agent_configuration,  **kwargs_)
supermod.OpenStackNetworkProvider.subclass = OpenStackNetworkProvider--super=types
# end class OpenStackNetworkProvider--super=types


class AgentConfiguration--super=types(supermod.AgentConfiguration):
    def __init__(self, network_mappings=None, broker_type=None, address=None, port=None, username=None, password=None, **kwargs_):
        super(AgentConfiguration--super=types, self).__init__(network_mappings, broker_type, address, port, username, password,  **kwargs_)
supermod.AgentConfiguration.subclass = AgentConfiguration--super=types
# end class AgentConfiguration--super=types


class OpenStackNetworkProviders--super=types(supermod.OpenStackNetworkProviders):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_network_provider=None, **kwargs_):
        super(OpenStackNetworkProviders--super=types, self).__init__(actions, size, total, active, openstack_network_provider,  **kwargs_)
supermod.OpenStackNetworkProviders.subclass = OpenStackNetworkProviders--super=types
# end class OpenStackNetworkProviders--super=types


class OpenStackNetwork--super=types(supermod.OpenStackNetwork):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, openstack_network_provider=None, **kwargs_):
        super(OpenStackNetwork--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, openstack_network_provider,  **kwargs_)
supermod.OpenStackNetwork.subclass = OpenStackNetwork--super=types
# end class OpenStackNetwork--super=types


class OpenStackNetworks--super=types(supermod.OpenStackNetworks):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_network=None, **kwargs_):
        super(OpenStackNetworks--super=types, self).__init__(actions, size, total, active, openstack_network,  **kwargs_)
supermod.OpenStackNetworks.subclass = OpenStackNetworks--super=types
# end class OpenStackNetworks--super=types


class DnsServers--super=types(supermod.DnsServers):
    def __init__(self, dns_server=None, **kwargs_):
        super(DnsServers--super=types, self).__init__(dns_server,  **kwargs_)
supermod.DnsServers.subclass = DnsServers--super=types
# end class DnsServers--super=types


class OpenStackSubnet--super=types(supermod.OpenStackSubnet):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, cidr=None, ip_version=None, gateway=None, dns_servers=None, openstack_network=None, **kwargs_):
        super(OpenStackSubnet--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, cidr, ip_version, gateway, dns_servers, openstack_network,  **kwargs_)
supermod.OpenStackSubnet.subclass = OpenStackSubnet--super=types
# end class OpenStackSubnet--super=types


class OpenStackSubnets--super=types(supermod.OpenStackSubnets):
    def __init__(self, actions=None, size=None, total=None, active=None, openstack_subnet=None, **kwargs_):
        super(OpenStackSubnets--super=types, self).__init__(actions, size, total, active, openstack_subnet,  **kwargs_)
supermod.OpenStackSubnets.subclass = OpenStackSubnets--super=types
# end class OpenStackSubnets--super=types


class KatelloErratum--super=types(supermod.KatelloErratum):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, title=None, type_=None, issued=None, severity=None, solution=None, summary=None, packages=None, host=None, vm=None, **kwargs_):
        super(KatelloErratum--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, title, type_, issued, severity, solution, summary, packages, host, vm,  **kwargs_)
supermod.KatelloErratum.subclass = KatelloErratum--super=types
# end class KatelloErratum--super=types


class KatelloErrata--super=types(supermod.KatelloErrata):
    def __init__(self, actions=None, size=None, total=None, active=None, katello_erratum=None, **kwargs_):
        super(KatelloErrata--super=types, self).__init__(actions, size, total, active, katello_erratum,  **kwargs_)
supermod.KatelloErrata.subclass = KatelloErrata--super=types
# end class KatelloErrata--super=types


class Packages--super=types(supermod.Packages):
    def __init__(self, package=None, **kwargs_):
        super(Packages--super=types, self).__init__(package,  **kwargs_)
supermod.Packages.subclass = Packages--super=types
# end class Packages--super=types


class Package--super=types(supermod.Package):
    def __init__(self, name=None, **kwargs_):
        super(Package--super=types, self).__init__(name,  **kwargs_)
supermod.Package.subclass = Package--super=types
# end class Package--super=types


class BrickProfileDetail--super=types(supermod.BrickProfileDetail):
    def __init__(self, profile_detail=None, brick=None, **kwargs_):
        super(BrickProfileDetail--super=types, self).__init__(profile_detail, brick,  **kwargs_)
supermod.BrickProfileDetail.subclass = BrickProfileDetail--super=types
# end class BrickProfileDetail--super=types


class Template--super=types(supermod.Template):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, status=None, memory=None, cpu=None, cpu_shares=None, bios=None, os=None, cluster=None, storage_domain=None, creation_time=None, origin=None, stateless=None, delete_protected=None, high_availability=None, display=None, sso=None, rng_device=None, console=None, timezone=None, domain=None, usb=None, soundcard_enabled=None, tunnel_migration=None, migration_downtime=None, virtio_scsi=None, serial_number=None, start_paused=None, cpu_profile=None, migration=None, io=None, custom_properties=None, custom_emulated_machine=None, custom_cpu_model=None, time_zone=None, small_icon=None, large_icon=None, memory_policy=None, vm=None, version=None, permissions=None, extensiontype_=None, **kwargs_):
        super(Template--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, status, memory, cpu, cpu_shares, bios, os, cluster, storage_domain, creation_time, origin, stateless, delete_protected, high_availability, display, sso, rng_device, console, timezone, domain, usb, soundcard_enabled, tunnel_migration, migration_downtime, virtio_scsi, serial_number, start_paused, cpu_profile, migration, io, custom_properties, custom_emulated_machine, custom_cpu_model, time_zone, small_icon, large_icon, memory_policy, vm, version, permissions, extensiontype_,  **kwargs_)
supermod.Template.subclass = Template--super=types
# end class Template--super=types


class InstanceType--super=types(supermod.InstanceType):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, type_=None, status=None, memory=None, cpu=None, cpu_shares=None, bios=None, os=None, cluster=None, storage_domain=None, creation_time=None, origin=None, stateless=None, delete_protected=None, high_availability=None, display=None, sso=None, rng_device=None, console=None, timezone=None, domain=None, usb=None, soundcard_enabled=None, tunnel_migration=None, migration_downtime=None, virtio_scsi=None, serial_number=None, start_paused=None, cpu_profile=None, migration=None, io=None, custom_properties=None, custom_emulated_machine=None, custom_cpu_model=None, time_zone=None, small_icon=None, large_icon=None, memory_policy=None, vm=None, version=None, permissions=None, **kwargs_):
        super(InstanceType--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, type_, status, memory, cpu, cpu_shares, bios, os, cluster, storage_domain, creation_time, origin, stateless, delete_protected, high_availability, display, sso, rng_device, console, timezone, domain, usb, soundcard_enabled, tunnel_migration, migration_downtime, virtio_scsi, serial_number, start_paused, cpu_profile, migration, io, custom_properties, custom_emulated_machine, custom_cpu_model, time_zone, small_icon, large_icon, memory_policy, vm, version, permissions,  **kwargs_)
supermod.InstanceType.subclass = InstanceType--super=types
# end class InstanceType--super=types


class WatchDog--super=types(supermod.WatchDog):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, template=None, instance_type=None, vms=None, vm=None, model=None, action=None, **kwargs_):
        super(WatchDog--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, template, instance_type, vms, vm, model, action,  **kwargs_)
supermod.WatchDog.subclass = WatchDog--super=types
# end class WatchDog--super=types


class WatchDogs--super=types(supermod.WatchDogs):
    def __init__(self, actions=None, size=None, total=None, active=None, watchdog=None, **kwargs_):
        super(WatchDogs--super=types, self).__init__(actions, size, total, active, watchdog,  **kwargs_)
supermod.WatchDogs.subclass = WatchDogs--super=types
# end class WatchDogs--super=types


class Feature--super=types(supermod.Feature):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, transparent_hugepages=None, gluster_volumes=None, vm_device_types=None, storage_types=None, storage_domain=None, nic=None, api=None, host=None, url=None, headers=None, **kwargs_):
        super(Feature--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, transparent_hugepages, gluster_volumes, vm_device_types, storage_types, storage_domain, nic, api, host, url, headers,  **kwargs_)
supermod.Feature.subclass = Feature--super=types
# end class Feature--super=types


class SchedulingPolicies--super=types(supermod.SchedulingPolicies):
    def __init__(self, actions=None, size=None, total=None, active=None, scheduling_policy=None, policy=None, **kwargs_):
        super(SchedulingPolicies--super=types, self).__init__(actions, size, total, active, scheduling_policy, policy,  **kwargs_)
supermod.SchedulingPolicies.subclass = SchedulingPolicies--super=types
# end class SchedulingPolicies--super=types


class Capabilities--super=types(supermod.Capabilities):
    def __init__(self, actions=None, size=None, total=None, active=None, version=None, permits=None, scheduling_policies=None, **kwargs_):
        super(Capabilities--super=types, self).__init__(actions, size, total, active, version, permits, scheduling_policies,  **kwargs_)
supermod.Capabilities.subclass = Capabilities--super=types
# end class Capabilities--super=types


class ProductInfo--super=types(supermod.ProductInfo):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, vendor=None, version=None, full_version=None, **kwargs_):
        super(ProductInfo--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, vendor, version, full_version,  **kwargs_)
supermod.ProductInfo.subclass = ProductInfo--super=types
# end class ProductInfo--super=types


class Version--super=types(supermod.Version):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, major=None, minor=None, build_=None, revision=None, full_version=None, extensiontype_=None, **kwargs_):
        super(Version--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, major, minor, build_, revision, full_version, extensiontype_,  **kwargs_)
supermod.Version.subclass = Version--super=types
# end class Version--super=types


class Statistics--super=types(supermod.Statistics):
    def __init__(self, actions=None, size=None, total=None, active=None, statistic=None, **kwargs_):
        super(Statistics--super=types, self).__init__(actions, size, total, active, statistic,  **kwargs_)
supermod.Statistics.subclass = Statistics--super=types
# end class Statistics--super=types


class Statistic--super=types(supermod.Statistic):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, values=None, type_=None, unit=None, disk=None, host=None, host_nic=None, host_numa_node=None, nic=None, vm=None, brick=None, step=None, gluster_volume=None, **kwargs_):
        super(Statistic--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, values, type_, unit, disk, host, host_nic, host_numa_node, nic, vm, brick, step, gluster_volume,  **kwargs_)
supermod.Statistic.subclass = Statistic--super=types
# end class Statistic--super=types


class Creation--super=types(supermod.Creation):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, status=None, fault=None, **kwargs_):
        super(Creation--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, status, fault,  **kwargs_)
supermod.Creation.subclass = Creation--super=types
# end class Creation--super=types


class Action--super=types(supermod.Action):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, async=None, grace_period=None, host=None, network=None, root_password=None, ssh=None, image=None, fence_type=None, ticket=None, proxy_ticket=None, iscsi=None, storage_domain=None, cluster=None, discard_snapshots=None, exclusive=None, vm=None, snapshot=None, template=None, host_nics=None, modified_network_attachments=None, removed_network_attachments=None, synchronized_network_attachments=None, modified_bonds=None, removed_bonds=None, modified_labels=None, removed_labels=None, check_connectivity=None, connectivity_timeout=None, virtual_functions_configuration=None, pause=None, force=None, option=None, fix_layout=None, brick=None, detach=None, clone=None, restore_memory=None, disks=None, succeeded=None, resolution_type=None, bricks=None, job=None, import_as_template=None, maintenance_enabled=None, storage_domains=None, disk=None, reason=None, logical_units=None, use_sysprep=None, use_cloud_init=None, certificates=None, status=None, fault=None, iscsi_target=None, power_management=None, is_attached=None, **kwargs_):
        super(Action--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, async, grace_period, host, network, root_password, ssh, image, fence_type, ticket, proxy_ticket, iscsi, storage_domain, cluster, discard_snapshots, exclusive, vm, snapshot, template, host_nics, modified_network_attachments, removed_network_attachments, synchronized_network_attachments, modified_bonds, removed_bonds, modified_labels, removed_labels, check_connectivity, connectivity_timeout, virtual_functions_configuration, pause, force, option, fix_layout, brick, detach, clone, restore_memory, disks, succeeded, resolution_type, bricks, job, import_as_template, maintenance_enabled, storage_domains, disk, reason, logical_units, use_sysprep, use_cloud_init, certificates, status, fault, iscsi_target, power_management, is_attached,  **kwargs_)
supermod.Action.subclass = Action--super=types
# end class Action--super=types


class SpecialObjects--super=types(supermod.SpecialObjects):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, **kwargs_):
        super(SpecialObjects--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link,  **kwargs_)
supermod.SpecialObjects.subclass = SpecialObjects--super=types
# end class SpecialObjects--super=types


class API--super=types(supermod.API):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, special_objects=None, product_info=None, summary=None, time=None, **kwargs_):
        super(API--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, special_objects, product_info, summary, time,  **kwargs_)
supermod.API.subclass = API--super=types
# end class API--super=types


class DetailedLink--super=types(supermod.DetailedLink):
    def __init__(self, href=None, rel=None, description=None, request=None, response=None, linkCapabilities=None, extensiontype_=None, **kwargs_):
        super(DetailedLink--super=types, self).__init__(href, rel, description, request, response, linkCapabilities, extensiontype_,  **kwargs_)
supermod.DetailedLink.subclass = DetailedLink--super=types
# end class DetailedLink--super=types


class GeneralMetadata--super=types(supermod.GeneralMetadata):
    def __init__(self, href=None, rel=None, description=None, request=None, response=None, linkCapabilities=None, name=None, **kwargs_):
        super(GeneralMetadata--super=types, self).__init__(href, rel, description, request, response, linkCapabilities, name,  **kwargs_)
supermod.GeneralMetadata.subclass = GeneralMetadata--super=types
# end class GeneralMetadata--super=types


class VersionCaps--super=types(supermod.VersionCaps):
    def __init__(self, actions=None, href=None, id=None, name=None, description=None, comment=None, creation_status=None, link=None, major=None, minor=None, build_=None, revision=None, full_version=None, current=None, features=None, cpus=None, power_managers=None, fence_types=None, storage_types=None, configuration_types=None, storage_domain_types=None, vm_types=None, boot_devices=None, display_types=None, nic_interfaces=None, os_types=None, disk_formats=None, graphics_types=None, disk_storage_types=None, disk_interfaces=None, vm_affinities=None, custom_properties=None, boot_protocols=None, error_handling=None, storage_formats=None, creation_states=None, power_management_states=None, host_states=None, external_statuses=None, host_protocols=None, host_non_operational_details=None, network_states=None, storage_domain_states=None, template_states=None, vm_states=None, vm_pause_details=None, disk_states=None, host_nic_states=None, data_center_states=None, vm_device_types=None, permits=None, scheduling_policies=None, usages=None, nfs_versions=None, pm_proxy_types=None, cpu_modes=None, sgio_options=None, watchdog_models=None, watchdog_actions=None, authentication_methods=None, kdump_states=None, spm_states=None, vm_pool_types=None, step_types=None, payload_encodings=None, gluster_volume_types=None, transport_types=None, gluster_volume_states=None, brick_states=None, reported_device_types=None, ip_versions=None, snapshot_statuses=None, content_types=None, hook_states=None, stages=None, sso_methods=None, architecture_capabilities=None, serial_number_policies=None, selinux_modes=None, rng_sources=None, scheduling_policy_unit_types=None, qos_types=None, inheritable_booleans=None, network_plugin_types=None, message_broker_types=None, display_disconnect_actions=None, quota_mode_types=None, **kwargs_):
        super(VersionCaps--super=types, self).__init__(actions, href, id, name, description, comment, creation_status, link, major, minor, build_, revision, full_version, current, features, cpus, power_managers, fence_types, storage_types, configuration_types, storage_domain_types, vm_types, boot_devices, display_types, nic_interfaces, os_types, disk_formats, graphics_types, disk_storage_types, disk_interfaces, vm_affinities, custom_properties, boot_protocols, error_handling, storage_formats, creation_states, power_management_states, host_states, external_statuses, host_protocols, host_non_operational_details, network_states, storage_domain_states, template_states, vm_states, vm_pause_details, disk_states, host_nic_states, data_center_states, vm_device_types, permits, scheduling_policies, usages, nfs_versions, pm_proxy_types, cpu_modes, sgio_options, watchdog_models, watchdog_actions, authentication_methods, kdump_states, spm_states, vm_pool_types, step_types, payload_encodings, gluster_volume_types, transport_types, gluster_volume_states, brick_states, reported_device_types, ip_versions, snapshot_statuses, content_types, hook_states, stages, sso_methods, architecture_capabilities, serial_number_policies, selinux_modes, rng_sources, scheduling_policy_unit_types, qos_types, inheritable_booleans, network_plugin_types, message_broker_types, display_disconnect_actions, quota_mode_types,  **kwargs_)
supermod.VersionCaps.subclass = VersionCaps--super=types
# end class VersionCaps--super=types


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'KeyValuePair'
        rootClass = supermod.KeyValuePair
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'KeyValuePair'
        rootClass = supermod.KeyValuePair
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'KeyValuePair'
        rootClass = supermod.KeyValuePair
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'KeyValuePair'
        rootClass = supermod.KeyValuePair
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
