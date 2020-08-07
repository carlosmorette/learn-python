import tornado.web
from jsonschema import validate, exceptions
import json
from pathlib import Path


class AppException(tornado.web.HTTPError):
    pass


class BaseRequestsHandler(tornado.web.RequestHandler):
    def cors_allowed_methods(self):
        return ["GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"]

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods",
                        ", ".join(self.cors_allowed_methods()))

    def post(self):
        self.write('some post')

    def get(self):
        self.write('some get')

    def options(self):
        self.set_status(204)
        self.finish()


def get_base_project_folder():
    cwd = Path.cwd()
    while cwd.name != "backend":
        cwd = cwd.parent
    return cwd


PROJECT_BASE_FOLDER = get_base_project_folder()


def validate_jsonschema(dict_for_validate: dict, schema_for_validate):
    print(schema_for_validate)

    with open(schema_for_validate) as desired_schema:
        try:
            return validate(dict_for_validate, json.load(desired_schema))
        except exceptions.ValidationError as error:
            return AppException(status_code=400, reason=str(error.message))
