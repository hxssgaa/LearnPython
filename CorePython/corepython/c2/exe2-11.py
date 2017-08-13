# Echo client program
import re
import socket

HOST = 'www.apple.com'  # The remote host
PORT = 80  # The same port as used by the server
BUFF_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s, open('apple.html', 'w') as f:
    s.connect((HOST, PORT))
    ipt = "GET / HTTP/1.1\nAccept: text/html\nHOST: %s\n\n" % HOST
    s.sendall(bytes(ipt, 'utf-8'))
    data = s.recv(BUFF_SIZE)
    c_len = 0
    m = re.search('Content-Length: (\d+)', data.decode('utf-8'))
    if m:
        c_len = int(m.group(1))
    print(c_len)
    while c_len > 0:
        data += s.recv(BUFF_SIZE if c_len >= BUFF_SIZE else c_len)
        c_len -= BUFF_SIZE
    f.write(data.decode('utf-8'))
