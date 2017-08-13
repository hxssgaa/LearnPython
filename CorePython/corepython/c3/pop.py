from poplib import POP3

POP3SVr = 'pop.126.com'

recvSvr = POP3(POP3SVr)
recvSvr.user('hxdavidtest001')
recvSvr.pass_('68671388aa')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index(b'')
recvBody = [e.decode('utf-8') for e in msg[sep + 1:]]
print(recvBody)
