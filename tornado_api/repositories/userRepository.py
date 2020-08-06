import tornado.web
from bson.json_util import dumps, loads
from utility.general import PROJECT_BASE_FOLDER, validate_jsonschema

class UserRepository(tornado.web.RequestHandler):
    db: str
    
    def __init__(self, db):
        self.db = db

    # list users
    async def get_users(self):
        users = self.db.users.find({})
        if not users:
            return dumps({})

        users = await users.to_list(length=10)
        return dumps(users)


    # post user
    async def post_user(self, data_post):
        schema_for_validate = f"{PROJECT_BASE_FOLDER}/schemas/user/userPost.json"

        validation = validate_jsonschema(data_post, schema_for_validate)

        if validation is None:
            self.db.users.insert_one({
                "firstName": data_post["firstName"],
                "lastName": data_post["lastName"],
                "age": data_post["age"]
            })

            return dumps({ "message": "Ok" })
        else:
            return dumps({ "error": str(validation) })