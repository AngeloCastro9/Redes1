import socket
from http import HTTPStatus

print("target host: ")
target_host = input() 
 
target_port = 80  # create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    client.connect((target_host,target_port))
    print("This's a valid server")
    print("Socket connected")
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    client.send(request.encode())  
    
    response = client.recv(4096)
    http_response = repr(response)
    http_response_len = len(http_response)
    http_response_len_kb = (http_response_len/1000)
    print(HTTPStatus.OK.value)
    print("[RECV] - length: %d" % http_response_len)
    print("Content length in Kb: %f" % http_response_len_kb)

except Exception as identifier:
    print("Host não encontrado!")
