import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write("Hello, world 3")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ], debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
