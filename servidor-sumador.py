#! /usr/bin/python3

import socket
import pickle

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)


def answer(objSocket, code, cookie, html):

    sending = 'HTTP/1.1 '
    if code == 200:
        sending = sending + '200 OK\r\n'
    else:
        sending = sending + '404 Not Found\r\n'

    if cookie:
        sending = sending + 'Set-Cookie: ' + cookie

    sending = sending + '\r\n\r\n' + html

    objSocket.send(bytes(sending, 'utf-8'))



try:
    while True:
        print('Waiting for connections...')
        (recvSocket, address) = mySocket.accept()
        petition = recvSocket.recv(2048).decode('utf-8')
        print(petition)
        recvOperand = int(petition.split()[1][1:]) # Operando que nos pasa el cliente
        if firstPetition:
            firstOperand = recvOperand
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><head>He recibido un " + str(firstOperand) +
            ".\r\nVuelveme a llamar con el segundo sumando</head></html>", 'utf-8'))
        else:
            result = firstOperand + recvOperand
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><head>Muchas gracias. \r\n" +
            str(firstOperand) + " + " + str(recvOperand) +
            " = " + str(result) +"</head></html>", 'utf-8'))

        recvSocket.close()
        firstPetition = not firstPetition

except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()
