from threading import Event, Thread
import socket

SERVER = socket.gethostbyname("")

print(f"Connecting to {SERVER} port {1234}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
	sock.connect((SERVER,1234))
	print("Connected")
	
except :
	print("connection refused")
	exit(0)
close = Event()
def receive():
	while not close.is_set():
		try :
			message = sock.recv(1024).decode('utf-8')
			print('\n' + message)
			print('\nClient$:',end='')
		except :
			continue
	sock.close()
def send():
	while True:
		message = input('Client:')
		sock.send(message.encode('utf-8'))
		if(message == "quit"):
			close.set()
			break
t1 = Thread(target = send)
t2 = Thread(target = receive)
t1.start()
t2.start()
