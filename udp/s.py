import socket
from threading import Thread
def send():
    while True:
        msg=input()
        s.sendto(msg.encode(),addr)
        if msg=="Exit":
            print("Server has closed .. ")
            break



def recieve():
    while True:
        data,addr=s.recvfrom(1024)
        print("\t\tClient: ",data.decode())
        if data.decode()=="Exit":
            print("Client has closed .. ")
            break
            

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',1042))

data,addr = s.recvfrom(1024)
print("Communicating with ",addr)
print("\t\tClient: ",data.decode())
t1=Thread(target=send)
t2=Thread(target=recieve)
t1.start()
t2.start()
t1.join()
t2.join()

s.close()