import socket
from threading import Thread

def receive():
    while True:
        try :
            message = sock.recv(1024).decode()
            print(message)
        except :
            continue
def send():
	while True:
		message = input()
		sock.send(message.encode())
		if(message == "quit"):
			break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1",1071))


t1 = Thread(target = send)
t2 = Thread(target = receive)
t1.start()
t2.start()