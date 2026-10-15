from checks.system import get_system_info, get_memory_info, get_disk_info
from checks.firewall import check_firewall
from checks.network import get_open_ports

# print the status of each Windows Firewall profile
def print_firewall_info(firewall):
    print("\nFIREWALL INFO")

    for firewall_info in firewall:
        # powershell returns 1 when the profile is enabled and 0 when it is disabled
        status = "Enabled" if firewall_info["Enabled"] == 1 else "Disabled"
        print(firewall_info["Name"], "-", status)


def print_listening_ports(listening_ports):
    print("\nLISTENING PORTS")

    if not listening_ports:
        print("No listening ports found.")
        return

    for item in listening_ports:
        print(
            f"{item['address']}:{item['port']} - "
            f"{item['process_name']} (PID: {item['pid']})"
        )

def main():
    while True:
# report an error and exit if response is not numeric 
        try:
            choice = int(input("Select an option:\n1. System Info\n2. Memory Info\n3. Disk Info\n4. Firewall Info\n5. Listening Ports\n6. All Info\n7. Exit\nEnter your choice: "))

        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        # Stop if the selected option is not in the menu
        if choice not in [1, 2, 3, 4, 5, 6, 7]:
            print("\nInvalid choice. Please select a valid option.")
            continue

        # run only the check selected by the user
        if choice == 1:
            info = get_system_info()
            print("\nSYSTEM INFO")
            print(info)

        elif choice == 2:
            memory = get_memory_info()
            print("\nMEMORY INFO")
            print(memory)

        elif choice == 3:
            disk = get_disk_info("C:\\")
            print("\nDISK INFO")
            # disk sizes are returned in bytes, divide by 1024**3 to display gigabytes
            print(f"Total: {disk['total'] / (1024 ** 3):.2f} GB")
            print(f"Used: {disk['used'] / (1024 ** 3):.2f} GB")
            print(f"Free: {disk['free'] / (1024 ** 3):.2f} GB")
            print(f"Percent: {disk['percent']}%")

        elif choice == 4:
            firewall = check_firewall()
            print_firewall_info(firewall)

        elif choice == 5:
            listening_ports = get_open_ports()
            print_listening_ports(listening_ports)

        elif choice == 6:
            # collect data from all five checks for the "all Info" option
            info = get_system_info()
            memory = get_memory_info()
            disk = get_disk_info("C:\\")
            firewall = check_firewall()
            listening_ports = get_open_ports()

            print("\nSYSTEM INFO")
            print(info)

            print("\nMEMORY INFO")
            print(memory)

            print("\nDISK INFO")
            
            print(f"Total: {disk['total'] / (1024 ** 3):.2f} GB")
            print(f"Used: {disk['used'] / (1024 ** 3):.2f} GB")
            print(f"Free: {disk['free'] / (1024 ** 3):.2f} GB")
            print(f"Percent: {disk['percent']}%")
            print_firewall_info(firewall)
            print_listening_ports(listening_ports)

        elif choice == 7:
            print("Exiting the program.")
            raise SystemExit


if __name__ == "__main__":
    main()