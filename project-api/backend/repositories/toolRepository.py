import tornado.web
from bson.json_util import dumps
from utility.general import PROJECT_BASE_FOLDER, validate_jsonschema


class ToolRepository():
    db: str

    def __init__(self, db):
        self.db = db

    async def list_tools(self):
        tools = self.db.tools.find({})

        if not tools:
            return dumps({})

        tools = await tools.to_list(length=100)

        return dumps(tools)

    async def register_tool(self, data_to_register):
        schema_for_validate = f"{PROJECT_BASE_FOLDER}/schemas/tool/toolPost.json"

        validation = validate_jsonschema(data_to_register, schema_for_validate)

        if validation is None:
            new_tool = self.db.tools.insert_one({
                "name": data_to_register["name"],
                "description": data_to_register["description"],
                "useful_links": data_to_register["useful_links"]
            })

            return dumps({"message": "Ok"})

        else:
            return dumps({"error": str(validation)})
