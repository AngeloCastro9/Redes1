import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
mensagem = b'oi'

destino = ('10.54.30.15', 8888)

client.sendto(mensagem, destino)
print("ihu")