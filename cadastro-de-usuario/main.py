import tornado.ioloop
import tornado.web
import json
import tornado


class User(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST')

    def save_user(self):
        with open("users.json") as users:
            print(json.load(users))

    def post(self):
        body = tornado.escape.json_decode(self.request.body)
        print(body)

def make_app():
    return tornado.web.Application([
        (r"/", User),
    ],autoreload=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
