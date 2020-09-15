import socket

from distlib.compat import raw_input

host = '172.20.10.3'  # 'localhost' # The server's hostname or IP address
port = 80  # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.settimeout(5.0)
try:
    client.connect((host, port))
except socket.error as e:
    print('Error: ' + str(e))
    client.close()


while True:
    str = raw_input("S: ")
    client.send(str.encode())
    if str == "Bye" or str == "bye":
        break
    #print("N: " + client.recv(1024).decode())

client.close()
