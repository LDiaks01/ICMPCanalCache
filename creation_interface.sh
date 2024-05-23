#!/bin/bash -x

NETWORK=10.87.87
MACHINE=$1
INTERFACE_ENTREE=injection
INTERFACE_SORTIE=canal

sudo ip l add dev $INTERFACE_ENTREE type veth peer name $INTERFACE_SORTIE
sudo ip a add dev $INTERFACE_SORTIE $NETWORK.$MACHINE/30
sudo ip l set dev $INTERFACE_ENTREE up
sudo ip l set dev $INTERFACE_SORTIE up