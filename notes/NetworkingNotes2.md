#Test 1 Review
1. A simple transition from zero to one includes how many frequencies?
  - An infinite number
2. I2C is what kind of communication?
  - Synchronous
3. A protocol transmits 1 byte at a time through a serial connection at 9600 bits per second with 1 start, 1 stop, and no parity bit. What is the minimum time it will take to transmit 72000 bytes or octets?
  - 75s - remember you are doing 9600 BITS not bytes so it is going to be really slow.
4. What is the lowest layer of the OSI 7-layer network diagram?
  - Physical
5. RS232 or 'Serial' port use a common ground and...
  - a transmit and a recieve wire.
6. what is the odd-parity of 0110?
  - 1
7. Bits or bytes of information to verify that both sides of a communication have the same data at the end of the reception are named?
  - CRC or Checksum
8. Bits or Bytes of data to synchronize the timing on both sides of a communication channel are usually named?
  - Framing
9. What is the second lowest layer of the OSI 7-layer Network?
  - Data Link
10. SPI uses a common ground and
  - A master in slave out, a master out slave in, a clock and a slave select.
11. RS-232 (Serial Ports) are
  - Still used even virtualized today
12. CRC stands for
  - cyclic redundancy check
13. If data is being transmitted at 9600 baud what is probably true about the wiring and hardware on both sides of the communication?
  - The wire and hardware can be poor quality.
14. A transmission approach that does not have a separate clock line is said to be?
  - asynchronous
15. FM communication
  - Changes frequency of the transmitted signal
16. SPI (Serial Peripheral interface) bus is an example of which type of communication?
  - Synchronous
17. AM communication
  - Changes volume of the transmitted signal
18. A simple on/off signal on a wire that a fixed frequency contains
  - infinite harmonics
19. I2C uses a common ground
  - a data and a clock wire
20. High speed data transmission
  - better quality wire/fiber optics and more precisely timed equipment
21. A transmission approach that does have a separate clock line is said to be
  - synchronous
22. Preamble bits or bytes are used to
  - synchronize timing and stabilize the AGC
23. SMTP stands for
  - A Simple Mail Transfer Protocol
24. Bits or bytes of nothing after data at the end of transmission are named?
  - Stop or Gap
25. To convert bps to Bps a quick rule is to
  - divide by 10 - you have to cover the start and stop bit which makes 10 total bits.
26. BAUD rate and bps would be different if
  - at any moment more than a single 1 or 0 is transmitted.

#Class Time
yeet
##OSI LAYERS
1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

###IP
- an ip is made up of 4 octets of bits. 127.0.0.1.
  They used to give an area a certain set of octets and left the remaining for the area to split up.
    People were assigned values on essentially a large binary tree that organized all the internet addresses
  There are not enough addresses to give everyone a unique address. it gives out the ip's based on the router.
  - Ping
    just sends some packet to someone else just to get a response and then time the response
###Sending Packets
  - packets are sent through a direction, there may be some routers that send it down 2 paths for optimal speeds. however they could arrive out of order and this would not be great. So if you do this make sure you have a protocol to arrange the packets in order.

- SCSI - this is a network standard pinout for most network drives
###DNS and DHCP
  - DHCP - assigns an IP address for a LAN
    - some things like a tv or printer you give a specific(static) ip on that because it would rarely move from that area but things like laptops and phones you need more of a dynamic ip so you use the DHCP to quickly give you an ip

###Internet Census 2012
  1. Introduction
  - It started because of some time spent on Nmap and they discovered over 100,000 vulnerable devices.
  2. Proof of concept
    - they created a small binary that could be uploaded to insecure devices
    - The binary consists of two parts
      1. The telnet scanner
        - which tries a few different login combinations, e.g root:root, admin:admin and both without passwords.
      2. the scanner manager,
        - this gives it IP ranges to scan and uploads scan results to a specified IP address.
    3. Design and Implementation
      - being nice
        - they did not want to damage the system or change anything so nothing was they only left a small README file that explained the project and a way to contact the source.
        -some of the devices had specific jobs: IPSec routes, BGP routes, x86 equipment with crypto accelerator cards, industrial control systems, physical door security systems, big Cisco/Juniper equipment.
          - all traffic was ignored.
      - Target Platforms
        - it only targeted devices with certain CPU and RAM requirements to avoid messing with industry or mission critical hardware.
        - the binary ran on approximately 420k devices.
          - 25% of all the unprotected devices found
        - C&C less Infrastructure
          - A classic botnet usually requires one or more command and control (C&C) servers the clients can connect to. A C&C server comes with several disadvantages
            1. Constant Updates
            2. Protection from abuse
            3. A Hosting Method that is both Secure and Anonymous
            - It is important to scan Port 23 for devices that have restarted.
        - Middle Nodes
          - accept data from the clients and keep it for download by the master server
            - IP addresses of the middle nodes were distributed to the clients by the master server when deploying a command.
    4. Deployment challenges

    5. Scanning Methods
      1. ICMP Ping
      2. Reverse DNS.
      3. Nmap
      4. Service Probes
      5. Traceroute
    6. Analysis
    7. Conclusion
####Wiki
  1. Data Collection
    - The data was collected by infilitrating internet devices, especially routes that used a defualt or no password at all.
    - named after Carna the roman goddess for protection of inner organs and health
    - compiled into a gif portrait to display internet use around the world, gathered data only included IPv4 and not IPv6.
    - because of the growing number of IPv6 another census will not be possible
  2. results
    - Carna found 1.3 billion addresses in use. the remaining 2.3 billion IPv4 are probaly not used.
    - USDHS LANDER-study counted 187 Million visible internet hosts in 2006
  3. Further Implications
    - The data provided by the Carna botnet was used by security researcher Morgan Marquis-Boire to determine how many countries FinFisher spyware was being used. The use of such legally-gray data to conduct open source analysis raised questions for some, but Marquis-Boire expressed a belief that data is data. "I consider this more like rogue academia rather than criminal activity," he told Wired Magazine
#Calculating Log
- to do log base anything you do.
	ln(number)/ln(base)

###Increasing the rate of routing
  Its an Algorithm
  - similar to Dijkstra's Algorithm
####ModBus
Modbus is a serial communications protocol originally published by Modicon (now Schneider Electric) in 1979 for use with its programmable logic controllers (PLCs). Modbus has become a de facto standard communication protocol and is now a commonly available means of connecting industrial electronic devices. The main reasons for the use of Modbus in the industrial environment are:

-  developed with industrial applications in mind,
-  openly published and royalty-free,
-  easy to deploy and maintain,
-  moves raw bits or words without placing many restrictions on vendors.
####MODBUS TCP
  - PoE - Power over ethernet
    - you put power on ethernet so that you have data and power going
    -  so you plug an ethernet connection in and you can contact any kind of sensor or lathe
    - Essentially is Modbus but with a TCP interface using ethernet.
    - allows us to send raw data bits over the ethernet to contact another device that is also drawing power.
###UDP
  - User datagram Protocol  
    - Software
  - Binding - when an executable claims a port to use when only that executable can use that port
Threading vs Process
  -  Thread and Process are two closely related terms in multi-threading. The main difference between the two terms is that the threads are a part of a process, i.e. a process may contain one or more threads, but a thread cannot contain a process.
- Ports
  - 0-1023 ports were super user access ports.
###Networking through coding
  - UDP client in c
    - steps server
      1. Socket
      2. SetSockopt
      3. Bind
      4. Listen
      5. Accept
      6. Send/Recieve

###Modem AT Commands
  - AT was used to tell the Modem Attention!
    - you follow AT wiht a + and then the command you want to be done
      - ex. AT+RESET
  - AT cellphone commands
    - there are huge text books just on the topic of this bullshit
    
