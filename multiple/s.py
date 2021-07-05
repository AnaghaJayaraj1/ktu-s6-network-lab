import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1034))
s.listen(5)
conn = []
print('Server is listening')
for i in range(3):
    con, addr = s.accept()
    conn.append(con)
while True:
    print('\nCommunicating with {0}\n'.format(addr))
    message = raw_input('Enter message : ')
    for i in range(3):
        conn[i].send(message)
s.close()
