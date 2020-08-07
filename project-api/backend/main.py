import tornado.ioloop
import tornado.web
import motor.motor_tornado
import json
from controllers.userController import UserController
from controllers.toolController import ToolController


def make_app(database):
    return tornado.web.Application([
        (r"/users", UserController),
        (r"/tools", ToolController)
    ],
        db=database["dev"]
    )


if __name__ == "__main__":

    with open('config.json') as config_api:
        string_conexao = json.load(config_api)

        db = motor.motor_tornado.MotorClient(string_conexao["string_conexao"])

        app = make_app(db)
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()
