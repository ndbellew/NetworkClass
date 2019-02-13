import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s".format(err))
port = 80
hostname = input("input host name you are trying to reach\n")
try:
    host_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()
s.connect((host_ip, port))
print("the socket has successfully connected to %s \n on port == %s" %(hostname, host_ip))
