from scapy.layers.inet import IP, TCP, UDP
from netfilterqueue import NetfilterQueue
import icmp_builder


def tracker(pkt):
    packet = IP(pkt.get_payload())
    if packet.haslayer(TCP):
        afficher_infos_paquet(packet)
        #handle_tcp_packet(packet)
    elif packet.haslayer(UDP):
        handle_udp_packet(packet)
    else:
        pass
        #print(packet.summary())
    pkt.drop()

def handle_tcp_packet(packet):
    tcp_layer = packet[TCP]
    ip_layer = packet[IP]
    src_ip = ip_layer.src
    src_port = tcp_layer.sport
    dst_ip = ip_layer.dst
    dst_port = tcp_layer.dport
    payload = ip_layer/tcp_layer
    #payload = tcp_layer.payload

    #send icmp packet with tcp payload as payload
    #icmp_builder.envoyer_paquets(payload)


    # Faire quelque chose avec les informations extraites
    print(f"TCP Packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
    #print("Payload:", payload)

    # Envoyer les données via une interface ou effectuer d'autres opérations nécessaires

def handle_udp_packet(packet):
    udp_layer = packet[UDP]
    ip_layer = packet[IP]
    src_ip = ip_layer.src
    src_port = udp_layer.sport
    dst_ip = ip_layer.dst
    dst_port = udp_layer.dport
    #create my own ip and udp layer
    payload = IP(src=src_ip, dst=dst_ip)/UDP(sport=src_port, dport=dst_port)/udp_layer.payload

    # Faire quelque chose avec les informations extraites
    print(f"UDP Packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")
    #print("Payload:", udp_layer.payload)

    #send icmp packet 
    icmp_builder.envoyer_paquets(payload)


def afficher_infos_paquet(paquet):
    # Vérifier si le paquet a une couche IP
    if IP in paquet:
        ip_src = paquet[IP].src
        ip_dst = paquet[IP].dst
        tos = paquet[IP].tos

        print(f"IP Source: {ip_src}")
        print(f"IP Destination: {ip_dst}")
        print(f"TOS: {tos}")

    # Vérifier si le paquet a une couche TCP
    if TCP in paquet:
        flags = paquet[TCP].flags
        seq = paquet[TCP].seq
        ack = paquet[TCP].ack

        print(f"TCP Flags: {flags}")
        print(f"TCP Sequence Number: {seq}")
        print(f"TCP Acknowledgment Number: {ack}")


nfqueue = NetfilterQueue()
nfqueue.bind(0, tracker)  # Le numéro de file d'attente doit correspondre à celui spécifié dans les règles iptables
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()

