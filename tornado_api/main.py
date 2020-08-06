import tornado.ioloop
import tornado.web
import motor.motor_tornado
import json
import controllers.userController

Controllers = {
    "UserController": controllers.userController.UserController
}


def make_app(database):
    return tornado.web.Application([
        (r"/", Controllers["UserController"])
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
  