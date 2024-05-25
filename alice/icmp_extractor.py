from scapy.all import *
from netfilterqueue import NetfilterQueue
import traceback
from ciphering import obfusquer_data, chiffrer_AES_256_CTR, dechiffrer_AES_256_CTR, read_key

INTERFACE_INJECTION='injection'
INTERFACE='canal'
ADRESSE_MAC=get_if_hwaddr(INTERFACE)


def handle_icmp_packet(pkt):
    # Vérifier si le paquet contient la couche ICMP
    try:
        packet = IP(pkt.get_payload())
        print("Packet:", packet.summary())
        if ICMP in packet:
            icmp_layer = packet[ICMP]
            if Raw in icmp_layer:
                # Récupérer le champ de charge utile (payload) du paquet ICMP
                payload = icmp_layer[Raw].load
                print("Payload ICMP après chiffrement :", payload)
                #payload = obfusquer_data(payload)
                payload = dechiffrer_AES_256_CTR(payload, read_key()[0], read_key()[1])
                print("Payload ICMP original :", payload)
                print("Taille du payload:", len(payload))
                
                # Analyser le payload pour extraire les couches IP et TCP
                ip_layer = IP(payload)
                if TCP in ip_layer:
                    afficher_infos_paquet(ip_layer)
                    tcp_layer = ip_layer[TCP]
                    # Maintenant vous avez accès aux couches IP et TCP extraites du payload ICMP
                    # Vous pouvez faire ce que vous voulez avec ces couches, par exemple, les imprimer
                    #print("IP Layer:", ip_layer.summary())
                    
                    print("TCP Layer:", tcp_layer.summary())
                    print("Payload:", tcp_layer.payload)
                    
                    #sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/IP(src=ip_layer[IP].src,dst=ip_layer[IP].dst)/tcp_layer/tcp_layer.payload,iface=INTERFACE_INJECTION)
                    sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/ip_layer,iface=INTERFACE_INJECTION)
                
                # pareil, verifier si UDP
                if UDP in ip_layer:
                    udp_layer = ip_layer[UDP]
                    print("IP Layer:", ip_layer.summary())
                    sendp(Ether(src=RandMAC(),dst=ADRESSE_MAC)/IP(src=ip_layer[IP].src,dst=ip_layer[IP].dst)
                    /UDP(sport=ip_layer[UDP].sport,dport=ip_layer[UDP].dport)/udp_layer.payload,iface=INTERFACE_INJECTION)
            else:
                print("No Raw layer in ICMP")

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        #pkt.accept()


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
nfqueue.bind(2, handle_icmp_packet)  # Le numéro de file d'attente doit correspondre à celui spécifié dans les règles iptables
try:
    nfqueue.run()
except KeyboardInterrupt:
    nfqueue.unbind()
