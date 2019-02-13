from scapy.all import *
import sys
me = "192.168.21.126"
target = ["192.168.21.197","192.168.21.215","192.168.21.212", "192.168.1.43"]
def Sniff_Packet(packet):
    if packet.haslayer(IP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        if pckt_dst not in ["224.0.0.251", "255.255.255.255", me] or pckt_src != me:
        #if pckt_dst == "192.168.21.215" or pckt_src=="192.168.21.215":
            print ("IP Packet:"+str(pckt_src)+" is going to "+str(pckt_dst)+" and has ttl value "+str(pckt_ttl))
        #if pckt_src in ["192.168.21.215"] or pckt_dst ==  "192.168.21.215":
            if pckt_src in target:
                packet.show()

def main():
    print("Custom packet sniffer")
    interface = "wlan0"
    if len(sys.argv)>1:
        if sys.argv[1] == "-iface":
            interface = sys.argv[2]
    sniff(filter="ip",iface="wlp3s0",prn=Sniff_Packet)

if __name__=="__main__":
    main()
