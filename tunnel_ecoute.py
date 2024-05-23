#!/usr/bin/python3


from scapy.all import *
INTERFACE_LAN='h1-eth0'
INTERFACE_VETH='injection'
def traiter_trame(t):
    print(t)


sniff(iface=[INTERFACE_VETH, INTERFACE_LAN],prn=traiter_trame,filter='tcp or (host 10.87.87.2 and udp)')