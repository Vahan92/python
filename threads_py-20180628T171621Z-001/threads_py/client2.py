import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

server_address = ('localhost', 10000)
print >>sys.stdout, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    message = 'clinet2!!!'
    print >>sys.stdout, 'sending "%s"' % message
    sock.sendall(message)
    count_received = 0
    count_expected = len(message)
    while count_received<count_expected:
        data = sock.recv(16)
        count_received += len(data)
        print >>sys.stdout, 'received "%s"' % data

finally:
    print>>sys.stdout, 'closing socket'
    sock.close()
