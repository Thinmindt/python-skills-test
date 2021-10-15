import tornado.ioloop
import tornado.websocket


class MainHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('Websocket opened')

    def on_message(self, message):
        self.write_message(f"Hello, world -- payload = {message}")

    def on_close(self):
        print('Websocket closed')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print('Server Shutting Down')
