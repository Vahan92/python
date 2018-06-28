from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True: 
        connection, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        connection.send(bytes("Hello! Enter your name!", "utf8"))
        addresses[connection] = client_address
        Thread(target=self.handle_client, args=(connection,)).start()


def handle_client(self,connection):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = connection.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type quit to exit.' % name
    connection.send(bytes(welcome,"utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg,"utf8"))
    clients[connection] = name
    while True:
        msg = connection.recv(16)
        print>>sys.stdout, 'received %s' % data
        if msg != bytes("{quit}"):
            broadcast(msg, name+": ")
        else:
            connection.send(bytes("{quit}"))
            connection.close()
            del clients[connection]
            print>>sys.stdout, 'no more data recieved from ',
            broadcast(bytes("%s has left the chat." % name))
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = 'localhost'
PORT = 10000
SERVER_ADDRESS = (HOST, PORT)
BUFSIZ = 1024
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)

if __name__ == "__main__":
    SERVER.listen(10)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
