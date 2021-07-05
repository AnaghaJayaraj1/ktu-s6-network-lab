
import socket
while True:
    sock = socket.socket()
    sock.connect(("127.0.0.1", 1034))
    msg = sock.recv(1024)
    print('messgae from server:',msg.decode())
    sock.close()






