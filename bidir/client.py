import socket
from threading import Thread
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1026))

def sendtoserver():
    while True: 
        msg=input()
        sock.send(msg.encode())
        if msg == "Exit":
            print("Client is closing")
            sock.close()

def recievefromserver():
    while True:
        msg1 = sock.recv(1036)
        print('\t\tMessage from server : {0}'.format(msg1.decode()))

t1=Thread(target=recievefromserver)
t2=Thread(target=sendtoserver)
t1.start()
t2.start()
t1.join()

t2.join()



