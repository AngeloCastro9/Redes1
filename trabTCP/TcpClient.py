# import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 80        # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     msg = input()
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))

# telnet program example
# import socket, select, string, sys

# #main function
# if __name__ == "__main__":
	
# 	if(len(sys.argv) < 3) :
# 		print ('Usage : python telnet.py hostname port')
# 		sys.exit()
	
# 	host = sys.argv[1]
# 	port = int(sys.argv[2])
	
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.settimeout(2)
	
# 	# connect to remote host
# 	try :
# 		s.connect((host, port))
# 	except :
# 		print ('Unable to connect')
# 		sys.exit()
	
# 	print ('Connected to remote host')
	
# 	while 1:
# 		socket_list = [sys.stdin, s]
		
# 		# Get the list sockets which are readable
# 		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
# 		for sock in read_sockets:
# 			#incoming message from remote server
# 			if sock == s:
# 				data = sock.recv(4096)
# 				if not data :
# 					print ('Connection closed')
# 					sys.exit()
# 				else :
# 					#print data
# 					sys.stdout.write(data)
			
# 			#user entered a message
# 			else :
# 				msg = sys.stdin.readline()
# 				s.send(msg)

























 # Socket client example in python

import socket
import sys  

host = '127.0.0.1'
port = 80  # web

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print("write a message from serve:")
request = input(0)
print('# Sending data to server')

try:
    bytes = request.encode(encoding='UTF-8')
    s.sendall(bytes)
except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(4096)
print(reply)