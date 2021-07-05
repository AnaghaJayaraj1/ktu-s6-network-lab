import socket
s = socket.socket()
s.bind(("127.0.0.1", 1034))
s.listen(5)
print('Server is listening')
while True:
    con,addr = s.accept()
    print('\nCommunicating with {0}\n'.format(addr))
    msg = input("Enter msg for client : ")
    con.send(msg.encode())
s.close()



