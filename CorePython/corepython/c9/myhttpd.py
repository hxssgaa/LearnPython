"""
This simple Web server can read GET requests, fetch a Web page (.html file),
and return it to the calling client.
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')  # Removing the leading '/'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    server = None
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'Welcome to the machine...'
        print 'Press ^C once or twice to quit.'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()
