from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class msg_server(Thread):
    def __init__(self, host, port,ser_add, server):
        self.Host = host
        self.Port = port
        self.SERVER_ADDRESS = ser_add
        self.SERVER = server
        self.clients = {}
        self.address = {}
        self.BUFSIZ = 1024

    def accept_incoming_connections(self):
        while True:
            print "Waiting for connection"
            connection, client_address = SERVER.accept()
            print connection, "connect\n"
            connection.send(bytes("Hello! Type your name and press enter!"))
            self.address[connection] = client_address
            Thread(target=self.handle_client, args=(connection,)).start()

    def handle_client(self,client):
        name = client.recv(BUFSIZ)
        welcome = "Welcome %s!" %name
        client.send(welcome)
        self.clients[client] = name
        while True:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}"):
                print msg
            else:
                client.send(bytes("{quit}"))
                client.close()
                del self.clients[client]
                break
    
    def msq_start(self):
        #SERVER.connect(SERVER_ADDRESS)
        SERVER.bind(SERVER_ADDRESS)
        SERVER.listen(5)
        print("Waiting for connection...")
        t = msg_server(HOST, PORT, SERVER_ADDRESS, SERVER)
        ACCEPT_THREAD = Thread(target=t.accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()

if __name__ == "__main__":

    HOST = 'localhost'
    PORT = 33001
    BUFSIZ = 1024
    SERVER_ADDRESS = (HOST, PORT)
    SERVER = socket(AF_INET, SOCK_STREAM)

    s = msg_server(HOST, PORT, SERVER_ADDRESS, SERVER)
    s.msq_start()
