import socket
s = socket.socket() #created socket
print("Socket created")
port = 2000 #create port at 2000 then bind.
s.bind(('',port))
print("Port created and binded")
#binded
s.listen(5)
print("Socket listening")
while True:
    c, addr = s.accept()
    print("Recieved connection fron %s" %(addr))
    c.send("Thank you for connecting")
    c.close()
