import socket

from distlib.compat import raw_input

host = 'localhost'  # '172.20.10.3'  # The server's hostname or IP address
port = 12345  # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
while True:
    str = raw_input("S: ")
    client.send(str.encode())
    if str == "Bye" or str == "bye":
        break
    print("N: " + client.recv(1024).decode())

client.close()
