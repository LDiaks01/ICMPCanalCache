#!/bin/bash -x

# bob is h3 and alice is h1
#authorize raw packet
sudo modprobe iptable_raw
sudo iptables -A PREROUTING -t raw -p tcp -j ACCEPT

# redirect packet to nfqueue rule
#paquets en entrée
sudo iptables -t raw -A PREROUTING -s 192.168.10.1 -p icmp -j NFQUEUE --queue-num 2

#paquets sortants
sudo iptables -t raw -A OUTPUT -d 10.87.87.1 -j NFQUEUE --queue-num 0


# udp command: socat - UDP4:10.87.87.1:6789,bind=10.87.87.2:6789    on h3

