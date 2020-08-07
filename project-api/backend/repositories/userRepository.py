import tornado.web
from bson.json_util import dumps
from utility.general import PROJECT_BASE_FOLDER, validate_jsonschema

class UserRepository():
    db: str
    
    def __init__(self, db):
        self.db = db

    # list users
    async def list_users(self):
        users = self.db.users.find({})
        if not users:
            return dumps({})

        users = await users.to_list(length=10)
        return dumps(users)


    # post user
    async def register_user(self, data_to_register):
        schema_for_validate = f"{PROJECT_BASE_FOLDER}/schemas/user/userPost.json"

        validation = validate_jsonschema(data_to_register, schema_for_validate)

        if validation is None:
            new_user = self.db.users.insert_one({
                "firstName": data_to_register["firstName"],
                "lastName": data_to_register["lastName"],
                "age": data_to_register["age"]
            })

            return dumps({ "message": "Ok" })
        else:
            return dumps({ "error": str(validation) })