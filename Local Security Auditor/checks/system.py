import platform 
import getpass
import psutil

def get_system_info():
    return {
        "computer": platform.node(),
        "user": getpass.getuser(),
        "os": platform.platform()
    }
def get_memory_info():
    memory = psutil.virtual_memory()
    return{
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "percent": memory.percent
    }

def get_disk_info(path = "/"):
    disk = psutil.disk_usage(path = path)
    
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }

