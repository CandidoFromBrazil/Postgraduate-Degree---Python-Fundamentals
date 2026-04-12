import psutil

'''You will need to install psutil via terminal/command prompt: pip install psutil, 
then upon running the code, it will display the network interfaces along with their corresponding IP and MAC addresses.'''

def get_network_info():
    print(f"{'Interface':<20} {'IP Address':<20} {'MAC Address'}")
    print("-" * 60)

    # Get all network interface addresses
    interfaces = psutil.net_if_addrs()

    for interface_name, addresses in interfaces.items():
        ip_address = "N/A"
        mac_address = "N/A"

        for addr in addresses:
            # Check for IPv4
            if addr.family == 2:  # socket.AF_INET
                ip_address = addr.address
            # Check for MAC address
            elif addr.family == -1: # psutil.AF_LINK (Hardware address)
                mac_address = addr.address

        # Only display interfaces that have an active IP or MAC
        if ip_address != "N/A" or mac_address != "N/A":
            print(f"{interface_name:<20} {ip_address:<20} {mac_address}")

if __name__ == "__main__":
    get_network_info()