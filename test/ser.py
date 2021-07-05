import socket
from threading import Thread

def rec(con, addr):
    print("Communicating with ", addr)

    while True:
        try:
            msg = con.recv(1024).decode()
            if(msg):
                if msg == "quit":
                    conn.remove(con)
                for client in conn:
                    if client == con:
                        continue
                    j=[]
                    j=msg.split()
                    print("Client: ")
                    for m in j:
                        print("\t",m)
                        client.send(m.encode())
        except :
            continue
    con.close()

conn = []


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1071))

s.listen()
print("Server is listening .. ")
while True:
    con, addr = s.accept()
    conn.append(con)
    t1 = Thread(target=rec, args=(con,addr))
    t1.start()

