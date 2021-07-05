import socket
from threading import Thread

def sendtoserver():
    while True:
        msg=input()
        sock.sendto(msg.encode(),(ip,addr))
        if msg == "Exit":
            print("Client is closing")
            break

def recievefromserver():
    while True:
        data,addr=sock.recvfrom(1024)
        if data.decode() == "Exit":
            print("Server has closed .. ")
            break
        else:
            print("\t\tServer : ",data.decode())
       

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="127.0.0.1"
addr = 1042

print("UDP client running ...\n")

t1=Thread(target=sendtoserver)
t2=Thread(target=recievefromserver)
t1.start()
t2.start()
t1.join()
t2.join()

sock.close()

