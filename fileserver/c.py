import socket

sock=socket.socket()
sock.connect(("127.0.0.1",1029))
print("Enter file name to display file content or enter 'quit' to exit\n")
while True:
    file=input(": ")
    sock.send(file.encode())
    if file=="quit":
        break
    else:
        msg = sock.recv(1024)
        if msg.decode()=="no":
            print("File does not exist ..")
        else:
            print(msg.decode()[0:-5])
            print("Pid: ",msg.decode()[-5:])
        
    
        