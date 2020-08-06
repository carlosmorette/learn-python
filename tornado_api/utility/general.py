import tornado.web
from jsonschema import validate, exceptions
import json
from pathlib import Path


class AppException(tornado.web.HTTPError):
    pass


def get_base_project_folder():
    cwd = Path.cwd()
    while cwd.name != "tornado_api":
        cwd = cwd.parent
    return cwd

PROJECT_BASE_FOLDER = get_base_project_folder()

def validate_jsonschema(dict_for_validate: dict, schema_for_validate):
    with open(schema_for_validate) as desired_schema:
        try:
            return validate(dict_for_validate, json.load(desired_schema))
        except exceptions.ValidationError as error:
            return AppException(status_code=400, reason=str(error.message))
