#! /usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)


try:
    while True:
        print('Waiting for connections...')
        (recvSocket, address) = mySocket.accept()
        petition = recvSocket.recv(2048).decode('utf-8')
        recvSocket.send(bytes('HTTP/1.1 404 Not Found', 'utf-8'))



        recvSocket.close()

except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()
