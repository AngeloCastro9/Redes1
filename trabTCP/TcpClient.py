import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

s.connect(("127.0.0.1" , 80))
s.sendall(input())
print(s.recv(4096))
s.close()