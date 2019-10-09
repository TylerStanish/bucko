import enum
import json
import os

from utils import fs


class Environments(enum.Enum):
    DEVELOPMENT = 'development'
    TESTING = 'testing'
    PRODUCTION = 'production'


def get_db_info() -> dict:
    """
    Gets the database info depending on FLASK_ENV
    """
    env = os.environ['FLASK_ENV']
    if env == Environments.DEVELOPMENT:
        return json.loads(read_from_file(fs.get_absolute_path()))

