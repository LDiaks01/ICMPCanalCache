from scapy.all import *
from ciphering import obfusquer_data, chiffrer_AES_256_CTR, dechiffrer_AES_256_CTR, read_key

# destination IP address
dst_ip = "192.168.10.1"
# Fonction pour envoyer des paquets ICMP avec un payload
def envoyer_paquets(payload):
    # Payload personnalisé
    #custom_payload = obfusquer_data(payload)
    # aes ciphering
    custom_payload = chiffrer_AES_256_CTR(payload, read_key()[0], read_key()[1])
    ping_packet = IP(dst=dst_ip)/ICMP()/custom_payload
    # Envoi du paquet
    #print(len(custom_payload))
    send(ping_packet)
    #print("Paquet envoyé avec succès.")

if __name__ == "__main__":
    pass