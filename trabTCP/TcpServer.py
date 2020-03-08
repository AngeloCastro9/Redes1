import socket
import datetime


TCP_IP = '127.0.0.1'
TCP_PORT = 80
BUFFER_SIZE = 1024

headers = """\
POST /auth HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

body = 'userName=Ganesh&password=pass'                                 
body_bytes = body.encode('ascii')
header_bytes = headers.format(
    content_type="application/x-www-form-urlencoded",
    content_length=len(body_bytes),
    host=str(TCP_IP) + ":" + str(TCP_PORT)
).encode('iso-8859-1')

payload = header_bytes + body_bytes


conn, addr = s.accept()

print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if data == b'\r\n':
        # conn.send(datetime.date.today() as bytes)
        conn.sendall(payload)
        conn.close()
    if not data: break
    conn.sendall(data)  # echo
conn.close()