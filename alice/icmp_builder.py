from scapy.all import *

# destination IP address
dst_ip = "192.168.10.3"
# Fonction pour envoyer des paquets ICMP avec un payload
def envoyer_paquets(payload):
    # Payload personnalisé
    custom_payload = payload
    ping_packet = IP(dst=dst_ip)/ICMP()/custom_payload
    # Envoi du paquet
    print(len(custom_payload))
    send(ping_packet)
    print("Paquet envoyé avec succès.")


if __name__ == "__main__":
    pass