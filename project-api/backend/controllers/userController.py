import tornado.web
from repositories.userRepository import UserRepository
from utility.general import BaseRequestsHandler


class UserController(BaseRequestsHandler):

    async def get(self):
        db = self.settings["db"]

        UserObject = UserRepository(db)
        UserObjectGet = await UserObject.list_users()
        self.write(UserObjectGet)

    async def post(self):
        db = self.settings["db"]
        body_request = tornado.escape.json_decode(self.request.body)

        UserObject = UserRepository(db)
        UserObjectPost = await UserObject.register_user(body_request)

        self.write(UserObjectPost)
