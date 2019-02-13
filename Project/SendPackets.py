from scapy.all import *

def main():
    send(IP(dst="192.168.1.7", src="10.11.12.14")/fuzz(UDP()/NTP(version=4)),loop=1)



if __name__=="__main__":
    main()
