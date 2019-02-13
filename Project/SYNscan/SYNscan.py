from scapy.all import *
import sys

def Classic_SYN_Scan(target, d_port):
    ans = sr1(IP(dst=target)/TCP(dport=d_port,flags="S"))
    ans.show()

def getHighLow():
    highlow = input("Please input Low to High port numbers\nex. 400 410\n")
    highlow = highlow.split()
    high = int(highlow[-1])
    low = int(highlow[0])
    return high,low

def Specific_Port_Scan():
    target=input("Please input target ip or address\n")
    dport_high,dport_low = getHighLow()
    ans,unans = sr(IP(dst=target)/TCP(sport=RandShort(), dport=(dport_low,dport_high), flags="S"))
    ans.summary()

def main():
    d_port = 80
    target= "www.example.com"
    if len(sys.argv) > 1:
            if sys.argv[1] == "classic":
                for i in range(2,len(sys.argv),1):
                    if sys.argv[i] == "-dp":
                        d_port = sys.argv[i+1]
                    elif sys.argv[i] == "-target":
                        target=sys.argv[i+1]
                    else:
                        Classic_SYN_Scan(target, d_port)
                        break
                Classic_SYN_Scan(target, d_port)

            elif sys.argv[1] == "-SP":
                Specific_Port_Scan()

            else:
                pass
    else:
        Classic_SYN_Scan(target,d_port)

if __name__=="__main__":
    main()
