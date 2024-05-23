from scapy.all import *
from netfilterqueue import NetfilterQueue

def print_packet(pkt):
    packet = IP(pkt.get_payload())
    print(packet.summary())
    pkt.drop()

nfqueue = NetfilterQueue()
nfqueue.bind(0, print_packet)  # Le numéro de file d'attente doit correspondre à celui spécifié dans les règles iptables
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()
