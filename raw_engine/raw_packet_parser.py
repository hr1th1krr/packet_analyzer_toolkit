import socket
import struct
from network_utilis import find_main_network_interface

""" GLOBAL VARIBLES """

main_network_card = find_main_network_interface()  # detect active/main NIC on user device

""" HANDLE NIC DETECTING ERROR """

if not main_network_card:  # terminate whole program if no NIC is detected
    exit()

""" ESTABLISH SOCKET & BIND SOCKET TO NIC """
try:
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(socket.ETH_P_ALL))  # establish socket to directly communicate with NIC to interpret and monitor packets.
    sniffer.bind((main_network_card, socket.ntohs(socket.ETH_P_ALL)))  # bind socket to the NIC
    
    print(f"[*]Socket sucessfully bound to: {main_network_card}")
    user_confirmation: str = input("Is this the correct network interface - [Y/N]: ")
    
    if user_confirmation.lower().strip() == "n":
        sniffer.close()  # closes the socket
        main_network_card = input("[*]Please enter the name of your network interface card: ")
        
        sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(socket.ETH_P_ALL))  # initiate a new socket 
        sniffer.bind((main_network_card, socket.ntohs(socket.ETH_P_ALL)))  # bind the new network interface and socket
        
        print(f"[*]Socket is now bound to {main_network_card}")

except PermissionError as p:
    print(f"[!]CRITICAL socket error: {p}")
    print("- Try run with SUDO!!!")
    exit()

except socket.error as e:  # catch any errors related to the socket
    print(f"[!]CRITICAL socket error: {e}")
