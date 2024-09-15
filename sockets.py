# server and clients 
# communication channels
# use for internet
import socket

# internet socket
# TCP protocol 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))

s.listen()

while True:
    client, address = s.accept()
    print("Connecting to {}".format(address))
    client.send("You are connected {}".endcode())
    client.close()
    