import socket
import sys
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 2003))
s.listen(5)
conn = []
def Pass(con,addr):
	while True:
		try:
			msg = con.recv(1024)
			for i in conn:
				if i!=con:
					i.send(msg)
			if msg.decode()=='quit':
				print(addr + 'has left the chat ..')
				conn.remove(con)
		except:
			break
def S():
	while True:
		msg=raw_input()
		if msg== 'quit':
			print("Server is closing .. ")
			break
print('Server running .. ')
while True:
	try:
		con, addr = s.accept()
		conn.append(con)
		t = Thread(target = Pass, args = (con,addr))
		t1=Thread(target=S)
		t1.start()
		t.start()
	except KeyboardInterrupt:
		break

t.join()
t1.join()
s.close()
sys.exit(1)