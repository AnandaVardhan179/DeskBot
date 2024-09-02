import psutil
import platform
from datetime import datetime

def get_system_info():
    system_info = {
        "platform": platform.system(),
        "platform-release": platform.release(),
        "platform-version": platform.version(),
        "architecture": platform.machine(),
        "hostname": platform.node(),
        "processor": platform.processor(),
        "ram": f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB",
        "boot-time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Get the network interface information dynamically
    net_info = psutil.net_if_addrs()
    for interface_name, interface_addresses in net_info.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                system_info["ip-address"] = address.address
            elif str(address.family) == 'AddressFamily.AF_LINK':
                system_info["mac-address"] = address.address

    return system_info

def get_cpu_info():
    cpu_info = {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": f"{psutil.cpu_freq().max:.2f}Mhz",
        "min_frequency": f"{psutil.cpu_freq().min:.2f}Mhz",
        "current_frequency": f"{psutil.cpu_freq().current:.2f}Mhz",
        "cpu_usage": f"{psutil.cpu_percent(interval=1)}%",
    }
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    memory_info = {
        "total": f"{svmem.total / (1024 ** 3):.2f} GB",
        "available": f"{svmem.available / (1024 ** 3):.2f} GB",
        "used": f"{svmem.used / (1024 ** 3):.2f} GB",
        "percentage": f"{svmem.percent}%",
    }
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        partition_info = {
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "fstype": partition.fstype,
        }
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            partition_info.update({
                "total_size": f"{partition_usage.total / (1024 ** 3):.2f} GB",
                "used": f"{partition_usage.used / (1024 ** 3):.2f} GB",
                "free": f"{partition_usage.free / (1024 ** 3):.2f} GB",
                "percentage": f"{partition_usage.percent}%",
            })
        except PermissionError:
            continue
        disk_info.append(partition_info)
    return disk_info

def get_network_info():
    net_io = psutil.net_io_counters()
    network_info = {
        "bytes_sent": f"{net_io.bytes_sent / (1024 ** 2):.2f} MB",
        "bytes_recv": f"{net_io.bytes_recv / (1024 ** 2):.2f} MB",
    }
    return network_info
