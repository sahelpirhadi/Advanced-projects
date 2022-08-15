from socket import *
ip=input("Please enter your target ip:")
port=int(input("Please enter your target port:"))
con=socket(AF_INET,SOCK_STREAM)
A=con.connect((ip,port))
if A==0:
    print("port open")
else:
    print("port close")
con.close()
