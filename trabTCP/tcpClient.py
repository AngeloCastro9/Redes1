import socket
from http import HTTPStatus
import requests

print("target host: ")
target_host = input()
print() #only to break line
target_port = 80  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    r = requests.get("https://"+target_host)
    client.connect((target_host,target_port))
    print("This's a valid server")
    print("Socket connected")

    try:
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    except Exception:
        print("Invalid Request!")

    client.send(request.encode())
    
    response = client.recv(4096)
    http_response = repr(response)
    http_response_len = len(http_response)
    http_response_len_kb = (http_response_len/1000)

    if r.headers['Content-Type']:
        print(r.headers['Content-Type'])

    print("HTTP Version: HTTP/1.1")
    print(r.status_code)

    if r.status_code == 200:
        print("200 OK")
    if r.status_code == 301:
        print("301 Moved Permanently")
    if r.status_code == 400:
        print("400 BAD REQUEST")
    if r.status_code == 404:
        print("404 Not Found")

    print("[RECV] - length: %d" % http_response_len)
    print("Content length in Kb: %f" % http_response_len_kb)

except ConnectionError as identifier:
    print("Host not found!")