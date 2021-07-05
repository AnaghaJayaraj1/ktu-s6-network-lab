import socket
import threading

SERVER = socket.gethostbyname("")

ListOfClient = []

lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, 1234))

def handle_client(conn, addr):
	print(f"{addr} connected")
	
	connected = True
	while connected:
		try:
			msg = conn.recv(1024).decode('utf-8')
			if(msg):
				if msg == "quit":
					ListOfClient.remove(conn)
					msg = f"{addr} user disconnected"
					connected = False
				message = f"<{addr[0]}> : {msg}"
				for client in ListOfClient:
					if client == conn:
						continue
					client.send(message.encode('utf-8'))
				print(message)
		except :
			continue
	conn.close()
def start():
	server.listen()
	print(f" Server is listing to {SERVER}")
	while True:
		conn, addr = server.accept()
		ListOfClient.append(conn)
		thread = threading.Thread(target=handle_client, args=(conn,addr))
		thread.start()
		print(f"ACTIVE CONNECTIONS :{threading.activeCount() - 1}")
print("Server is starting...")
start()
