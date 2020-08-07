import tornado.web
from utility.general import BaseRequestsHandler
from repositories.toolRepository import ToolRepository


class ToolController(BaseRequestsHandler):

    async def get(self):
        db = self.settings["db"]

        ToolObject = ToolRepository(db)
        ToolObjectGet = await ToolObject.list_tools()
        self.write(ToolObjectGet)

    async def post(self):
        db = self.settings["db"]
        body_request = tornado.escape.json_decode(self.request.body)

        ToolObject = ToolRepository(db)
        ToolObjectPost = await ToolObject.register_tool(body_request)

        self.write(ToolObjectPost)
