import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item1", "Item2", "Item3"]
        # self.render("template.html", title="Templete Teste", items=items)
        nome = "Carlos"
        self.render("template.html", nome=nome, title=nome)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ], autoreload=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()