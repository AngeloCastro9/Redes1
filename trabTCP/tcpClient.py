import socket
import sys

target_host = sys.argv[1]
print() #only to break line
target_port = 80  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    client.connect((target_host,target_port))
    print("This's a valid server")
    print("Socket connected")

    try:
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    except Exception:
        print("Invalid Request!")

    client.send(request.encode())
    
    response = client.recv(1024)
    http_response = repr(response)
    http_response_len = len(http_response)
    http_response_len_kb = (http_response_len/1000)

    print("HTTP version: " + response.decode()[5:8])
    print("Code: " + response.decode()[9:12])
    if response.decode()[9:12] == '200':
        print("200 OK")
    if response.decode()[9:12] == '301':
        print("301 Moved Permanently")
    if response.decode()[9:12] == '400':
        print("400 BAD REQUEST")
    if response[9:12] == b'404':
        print("404 Not Found")  

    ct = response.decode().find("Content-Type")
    if ct > 1:
        print(response.decode()[ct:ct+25])

    print("[RECV] - length: %d" % http_response_len)
    print("Content length in Kb: %f" % http_response_len_kb)

except Exception as identifier:
    print("Host not found!")