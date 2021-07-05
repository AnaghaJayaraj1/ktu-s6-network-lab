from threading import Thread
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1041))
def requestFile():
    while True:
        try:
            file = raw_input("\nEnter filename\n")
            if file == 'quit':
                sock.send(file)
                break
            else:
                sock.send(file)
                content = sock.recv(1024)
            if content == "Try again":
                print("File not found")
            else:
                print("\nReceived\n\n{}".format(content))
        except:
            break
t = Thread(target = requestFile)
t.start()
t.join()
sock.close()