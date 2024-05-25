from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom


# read the key and nonce from the file
def read_key():
    with open("aes_key.txt", "rb") as f:
        cle = f.readline().strip()
        iv = f.readline().strip()
    return cle, iv

# Chiffrer des données avec AES en mode CTR
def chiffrer_AES_256_CTR(payload, cle, iv):
    payload = bytes(payload)
    cipher = Cipher(algorithms.AES(cle), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    donnees_chiffrees = encryptor.update(payload) + encryptor.finalize()
    return donnees_chiffrees

# Déchiffrer des données avec AES en mode CTR
def dechiffrer_AES_256_CTR(donnees_chiffrees, cle, iv):
    cipher = Cipher(algorithms.AES(cle), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    payload = decryptor.update(donnees_chiffrees) + decryptor.finalize()
    return payload

# Fonction pour obfusquer les données en inversant les bits avec XOR
def obfusquer_data(payload):
    bytes_payload = bytes(payload)
    return bytes([b ^ 0xFF for b in bytes_payload])