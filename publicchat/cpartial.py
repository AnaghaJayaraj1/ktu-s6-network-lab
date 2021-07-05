from threading import Thread
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',2003))
def send():
	while True:
		
		message=raw_input()
		sock.send(message.encode())
		if message == 'quit':
			print('Client is closing ..')
			break

def receive():
	while True:
		message = sock.recv(1024)
		print('\t\t\tMessage Received: ' + message.decode())
		
	
print('\nEnter message: ')	
t1 = Thread(target =  send)
t1.start()
t2 = Thread(target = receive)


t2.start()

t1.join()
t2.join()
sock.close()
