from smtplib import SMTP as smtp

s = smtp('smtp.126.com')
s.login('hxdavidtest001', '68671388aa')
s.set_debuglevel(1)
s.sendmail('hxdavidtest001@126.com', ('hxdavidtest001@126.com', 'hxdavidtest002@126.com'), ''' \
From: hxdavidtest001@126.com\r\nTo:hxdavidtest001@126.com, hxdavidtest002@126.com\r\nSubject: test email\r\n\r\nxxx \
asdasdasda\r\n.''')
