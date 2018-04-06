import socket                 
import ipaddress
import time


s = socket.socket()       

csock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
csock.bind(("",5000))
csock.setblocking(0)
message=[]
while True:
    try:
        cs = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        cs.sendto("found".encode(), ('255.255.255.255', 10000))
        message=csock.recvfrom(1024)
        break
    except:
        pass
string=message[1][0]
print(string)

time.sleep(5)

port = 10000    
s.connect((string, port))
s.send("Hello server!".encode())

filename=s.recv(1024).decode()
filesize=s.recv(1024).decode()
filename=filename+" download"
with open(filename, 'wb') as f:
    print ('file opened')
    print('receiving data...')
    while True:
        data = s.recv(int(filesize))
        if not data:
            break
        # write data to a file
        f.write(data)
print('Successfully get the file')
s.close()
print('connection closed')