# benodigde libraries 
import atexit
import configparser
from pyVim import connect
from pyVmomi import vmodl
from pyVim.connect import Disconnect
import humanize
import sys

# config file
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

# gebruik printen in .txt file
f = open("gebruik.txt", 'w')
sys.stdout = f

MBFACTOR = float(1 << 20)

printVM = True
printDatastore = True
printHost = True

# opvragen data van vSphere
def head():
    try:
        si = connect.ConnectNoSSL(host= (config['NETLAB'].get('host')), port= 443, 
        user= (config['NETLAB'].get('username')), pwd= (config['NETLAB'].get('password')))
        
        atexit.register(Disconnect, si)
        content = si.RetrieveContent()

        for datacenter in content.rootFolder.childEntity:
            print ("Datacenter: " + datacenter.name)

            if printDatastore:
                datastores = datacenter.datastore
                for ds in datastores:
                    data_store(ds)

            if printHost:
                if hasattr(datacenter.vmFolder, 'childEntity'):
                    hostFolder = datacenter.hostFolder
                    computeResourceList = hostFolder.childEntity

                    for computeResource in computeResourceList:
                        data_res(computeResource)

    except vmodl.MethodFault as e:
        print ("Fout:Controlleer je verbinding met de Cisco VPN en je inloggegevens van Vcenter!", e)


# data van de data store
def data_store(datastore):
    try:
        summary = datastore.summary
        capacity = summary.capacity
        freeSpace = summary.freeSpace
        uncommittedSpace = summary.uncommitted
        freeSpacePercentage = (float(freeSpace) / capacity) * 100

        print ("\nDatastore name: ", summary.name)
        print ("Capacity: ", humanize.naturalsize(capacity, binary=True))

        if uncommittedSpace is not None:
            provisionedSpace = (capacity - freeSpace) + uncommittedSpace

            print ("Provisioned space: ", humanize.naturalsize(provisionedSpace, binary=True))
            print ("Free space: ", humanize.naturalsize(freeSpace, binary=True))
            print ("Free space percentage: " + str(freeSpacePercentage) + "%")
       

    except Exception:
        print ("De summary kan niet geopend worden!: ", datastore.name)
       
        pass

# data gebruik resources
def data_res(computeResource):
    try:
        hostList = computeResource.host
        for host in hostList:
            data_host(host)

    except Exception:
        print ("Informatie hierover kan niet opgehaald worden!:", computeResource.name)
       
        pass

# data van de host
def data_host(host):
    try:
        summary = host.summary
        stats = summary.quickStats
        hardware = host.hardware
        cpuCapacityMhz = (host.hardware.cpuInfo.hz * host.hardware.cpuInfo.numCpuCores) / 1000 / 1000
        cpuUsage = stats.overallCpuUsage
        memoryCapacity = hardware.memorySize
        memoryCapacityInMB = hardware.memorySize/MBFACTOR
        memoryUsage = stats.overallMemoryUsage
        freeMemoryPercentage = 100 - ((float(memoryUsage) / memoryCapacityInMB) * 100)

        print ("--------------------------------------------------")
        print ("Host name: ", host.name)
        print ("Host CPU capacity: ", cpuCapacityMhz, " Mhz")
        print ("Host CPU usage: ", cpuUsage)
        print ("Host memory capacity: ", humanize.naturalsize(memoryCapacity, binary=True))
        print ("Host memory usage: ", memoryUsage / 1024, "GB")
        print ("Free memory percentage: " + str(freeMemoryPercentage) + "%")
        print ("--------------------------------------------------")

    except Exception:
        print ("De host kan niet gepingd worden!:", host.name)
        
        pass
      
if __name__ == "__main__":

    head()
    f.close()
