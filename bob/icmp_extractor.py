from scapy.all import *
from netfilterqueue import NetfilterQueue
import traceback

INTERFACE_INJECTION='injection'
INTERFACE='canal'
ADRESSE_MAC=get_if_hwaddr(INTERFACE)


def handle_icmp_packet(pkt):
    # Vérifier si le paquet contient la couche ICMP
    try:
        packet = IP(pkt.get_payload())
        #print("Packet:", packet.summary())
        if ICMP in packet:
            icmp_layer = packet[ICMP]
            if Raw in icmp_layer:
                # Récupérer le champ de charge utile (payload) du paquet ICMP
                payload = icmp_layer[Raw].load
                #print("Payload ICMP:", payload)
                #print("Taille du payload:", len(payload))
                
                # Analyser le payload pour extraire les couches IP et TCP
                ip_layer = IP(payload)
                if TCP in ip_layer:
                    
                    tcp_layer = ip_layer[TCP]
                    # Maintenant vous avez accès aux couches IP et TCP extraites du payload ICMP
                    # Vous pouvez faire ce que vous voulez avec ces couches, par exemple, les imprimer
                    print("IP Layer:", ip_layer.summary())
                    
                    print("TCP Layer:", tcp_layer.summary())
                    
                    sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/ip_layer/tcp_layer,iface=INTERFACE_INJECTION)
                
                # pareil, verifier si UDP
                if UDP in ip_layer:
                    udp_layer = ip_layer[UDP]
                    #print("IP Layer:", ip_layer.summary())
                    sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/IP(src=ip_layer[IP].src,dst=ip_layer[IP].dst)
                    /UDP(sport=ip_layer[UDP].sport,dport=ip_layer[UDP].dport)/udp_layer.payload,iface=INTERFACE_INJECTION)
            else:
                print("No Raw layer in ICMP")

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        #pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(2, handle_icmp_packet)  # Le numéro de file d'attente doit correspondre à celui spécifié dans les règles iptables
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()
