from threading import Thread
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('127.0.0.1',1053)


def request(addr):
    while True:
        try:
            ch = raw_input("\nType 'time' to fetch current time or 'quit' to exit: ")
            if ch == 'time':
                msg = "Fetching Current Time ........"
                sock.sendto(msg,addr)
                t,addr = sock.recvfrom(1024)
                print("Current Time is: " + t)
            elif ch == 'quit':
                break
        except:
            continue
request(addr)
sock.close()