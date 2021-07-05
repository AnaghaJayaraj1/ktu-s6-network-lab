import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1034))
while True:
    
    msg = sock.recv(1024)
    print('Message received : {0}'.format(msg))
sock.close()




