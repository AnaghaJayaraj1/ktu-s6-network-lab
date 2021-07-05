import os, sys
rd, wd = os.pipe()
pid = os.fork()


if pid>0:
    os.close(wd)
    fr1=os.fdopen(rd, "r")
    str=fr1.read()
    print("Msg from child : ",str)
    pid2=os.getpid()
    print("PID of parent process:",pid2)
    
   
else:
    os.close(rd)
    fw1=os.fdopen(wd,"w")
    msg = input("Enter message: ")
    pid1=os.getpid()
    print("PID of child process:",pid1)
    fw1.write(msg)
 


