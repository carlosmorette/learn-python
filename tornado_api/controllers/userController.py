import tornado.web
from repositories.userRepository import UserRepository

class UserController(tornado.web.RequestHandler):
    
    async def get(self):
        db = self.settings["db"]

        UserObject = UserRepository(db)
        UserObjectGet = await UserObject.get_users()
        self.write(UserObjectGet)


    async def post(self):
        db = self.settings["db"]
        body_request = tornado.escape.json_decode(self.request.body)

        UserObject = UserRepository(db)
        UserObjectPost = await UserObject.post_user(body_request)
        
        self.write(UserObjectPost)