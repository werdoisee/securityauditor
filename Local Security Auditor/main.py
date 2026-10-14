from checks.system import get_system_info, get_memory_info, get_disk_info
from checks.firewall import check_firewall


# print the status of each Windows Firewall profile
def print_firewall_info(firewall):
    print("\nFIREWALL INFO")

    for firewall_info in firewall:
        # powershell returns 1 when the profile is enabled and 0 when it is disabled
        status = "Enabled" if firewall_info["Enabled"] == 1 else "Disabled"
        print(firewall_info["Name"], "-", status)


# report an error and exit if response is not numeric 
try:
    choice = int(input("Select an option:\n1. System Info\n2. Memory Info\n3. Disk Info\n4. Firewall Info\n5. All Info\nEnter your choice: "))

except ValueError:
    print("Invalid input. Please enter a number.")
    raise SystemExit

# Stop if the selected option is not in the menu
if choice not in [1, 2, 3, 4, 5]:
    print("Invalid choice. Please select a valid option.")
    raise SystemExit

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
    # collect data from all four checks for the "all Info" option
    info = get_system_info()
    memory = get_memory_info()
    disk = get_disk_info("C:\\")
    firewall = check_firewall()

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