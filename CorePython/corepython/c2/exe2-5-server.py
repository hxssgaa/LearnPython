# Echo server program
import os
import socket
from time import ctime

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port


def handle_command(cmd):
    return {
        'date': ctime(),
        'os': os.name,
        'ls': str(os.listdir(os.curdir))
    }.get(cmd, 'Command not found.')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(bytes(handle_command(data.decode('utf-8')), 'utf-8'))
