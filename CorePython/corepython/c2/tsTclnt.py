from socket import *

HOST = 'localhost'
PORT = 21567
BUFF_SIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFF_SIZE)
    if not data:
        break
    print(data.decode('utf-8'))
