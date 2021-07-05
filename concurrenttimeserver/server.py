from threading import Thread
import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',1053))


#def stop():
    #while True:
      #  try:
       #     t = time.asctime()
       #     s.sendto(t,addr)
       # except:
       #     break

while True:
    try:
        data,addr = s.recvfrom(1024)
        t = time.asctime()
        s.sendto(t,addr)
        
        #TimeService(addr)
        #t.start()
    except KeyboardInterrupt:
        break
s.close()



