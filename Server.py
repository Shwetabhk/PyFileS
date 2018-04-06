import socket                   # Import socket module
import os
import time

port = 10000                   # Reserve a port for your service.
s = socket.socket()   
s.bind(("", port))
s.listen(5)
print ('Server listening....')
while True:
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(("",10000))
    print("Finding Server...........................") 
    message=sock.recvfrom(1024)
    sock.sendto("Found".encode(),(message[1][0],5000))
    string=message[1][0]
    print(string)
    conn, addr = s.accept()     # Establish connection with client.
    print (conn)
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename=input("Enter the file name  :  ")
    conn.send(filename.encode())
    time.sleep(2)
    size=os.stat(filename).st_size
    conn.send(str(size).encode())
    print (size)
    with open(filename,"rb") as f:
        l = f.read(size) 
        while (l):
            conn.send(l)
        #print('Sent ',repr(l))
            l = f.read(100000000)
    time.sleep(3)  
    print('Done sending')
    conn.close()