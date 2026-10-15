import psutil


def get_open_ports():
    connections = psutil.net_connections(kind="inet")
    ports = []

    for connection in connections:
        if connection.status != psutil.CONN_LISTEN or not connection.laddr:
            continue

        pid = connection.pid
        process_name = "Unknown"

        if pid is not None:
            try:
                process_name = psutil.Process(pid).name()
            except psutil.NoSuchProcess:
                process_name = "Process has already terminated"
            except psutil.AccessDenied:
                process_name = "Access denied to process information"

        ports.append({
            "address": connection.laddr.ip,
            "port": connection.laddr.port,
            "pid": pid,
            "process_name": process_name,
        })

    return sorted(ports, key=lambda item: (item["port"], item["address"]))
