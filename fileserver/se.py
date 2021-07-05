from threading import Thread
import socket
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1041))
s.listen(5)
def fileRead(con, addr):
    while True:
        try:
            fileName = con.recv(1024)
            if fileName == 'quit':
                break
            else:
                fhandle = open(fileName)
                content = fhandle.read()
                pid = os.getpid()
                msg = "pid: {}\n{}".format(pid,content)
                con.send(msg)
                fhandle.close()
        except:
            con.send("Try again")
while True:
    try:
        con, addr = s.accept()
        print("Accepted connection from "+addr[0])
        t = Thread(target = fileRead, args = (con,addr))
        t.start()
    except KeyboardInterrupt:
        break
s.close()

