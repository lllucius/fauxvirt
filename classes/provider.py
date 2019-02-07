from abc import ABC, abstractmethod

class ProviderBase(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def terminate(self):
        pass

    @abstractmethod
    def get_api(self):
        pass

    @abstractmethod
    def get_apisummary(self):
        pass

    @abstractmethod
    def get_clusters(self):
        pass

    @abstractmethod
    def get_cluster(self, guid):
        pass

    @abstractmethod
    def get_datacenters(self):
        pass

    @abstractmethod
    def get_datacenter(self, guid):
        pass

    @abstractmethod
    def get_disks(self):
        pass

    @abstractmethod
    def get_disk(self, guid):
        pass

    @abstractmethod
    def get_files(self):
        pass

    @abstractmethod
    def get_file(self, guid):
        pass

    @abstractmethod
    def get_hosts(self):
        pass

    @abstractmethod
    def get_host(self, guid):
        pass

    @abstractmethod
    def get_networks(self):
        pass

    @abstractmethod
    def get_network(self, guid):
        pass

    @abstractmethod
    def get_storagedomains(self):
        pass

    @abstractmethod
    def get_storagedomain(self, guid):
        pass

    @abstractmethod
    def get_vms(self):
        pass

    @abstractmethod
    def get_vm(self, guid):
        pass

    @abstractmethod
    def get_templates(self):
        pass

    @abstractmethod
    def get_template(self, guid):
        pass

