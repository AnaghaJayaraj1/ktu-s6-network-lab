import socket
from threading import Thread
import os
def sendfile(con,addr):
    while True:
        filename = con.recv(1027).decode()
        if filename=="quit":
            print("Client ",addr," has left ...")
            break
        else:
            try:    
                fhandle=open(filename)
                data=fhandle.read()
                con.send(data.encode())
                id=os.getpid()
                con.send(str(id).encode())
                
            except FileNotFoundError:
                m="no"
                con.send(m.encode())
        
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.01",1029))
s.listen(5)
print("Server is listening ..")

while True:
    con,addr = s.accept()
    print("Server communicating with",addr)
    t1=Thread(target=sendfile,args=(con,addr))
    t1.start()


s.close()