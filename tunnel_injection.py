#!/usr/bin/python3
from scapy.all import *
INTERFACE_INJECTION='injection'
INTERFACE='canal'
ADRESSE_MAC=get_if_hwaddr(INTERFACE)
# Injection de paquets UDPs
sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/IP(src='10.87.87.1',dst='10.87.87.2')/
UDP(sport=5678,dport=6789)/"Hello",iface=INTERFACE_INJECTION)
# Injection de paquets TCPs
sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/IP(src='10.87.87.1',dst='10.87.87.2')/
TCP(sport=5678,dport=6789,flags='S'),iface=INTERFACE_INJECTION)