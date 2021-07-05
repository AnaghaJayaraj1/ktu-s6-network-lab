import socket
from threading import Thread
def send():
    while True:
        msg=input()
        con.send(msg.encode())
        #print('\nCommunicating with {0}'.format(addr))

def recieve():
    while True:
        msg1 = con.recv(1026)
        print('\t\tMessage from client : {0}'.format(msg1.decode()))
        if msg1==b"Exit":
            print("Client has closed .. ")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1026))
s.listen(5)
print('Server is listening')

con,addr=s.accept()
t1=Thread(target=send)
t2=Thread(target=recieve)
t1.start()
t2.start()

t1.join()
t2.join()
s.close()  
    
    
