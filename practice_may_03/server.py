import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print("Connection from {address} has been established.")
    clientsocket.send(bytes("Hey Abeer,What's up Man!!!","utf-8"))
