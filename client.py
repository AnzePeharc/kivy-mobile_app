import socket


host = '172.20.10.3'  # The server's hostname or IP address
port = 12345  # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("I am CLIENT<br>".encode("utf-8"))
from_server = client.recv(4096)
client.close()
print(from_server)


