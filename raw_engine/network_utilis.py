import socket

""" check if current network interface name is acitve or not"""

def all_network_interface(interface_name):
    try:
        network_interface_path = f"/sys/class/net/{interface_name}/operstate"  # declare directory path to the state of the current network interface
        with open(network_interface_path, "r") as f:
            state = f.read().strip()  # remove unwanted elements from contents
            return state == "up"  # returns True if network interface is active
    except FileNotFoundError as e:
        print("FILE COULD NOT BE FOUND")
    return False  # returns False if network interface is not active

""" filter out the active/running network interface"""

def find_main_network_interface():
    list_all_NIC = socket.if_nameindex()  # list all available network interfaces. OUTPUT_EXAMPLE - [(index int, name string)]
    for index, name in list_all_NIC:
        if all_network_interface(name):# returns the name of NIC if current network interface is active (UP)
            return name
    print("NIC not detected")
    return None