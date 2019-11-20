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
    if env == Environments.PRODUCTION.value:
        return {
            'dbname': os.environ['DBNAME'],
            'user': os.environ['DBUSER'],
            'host': os.environ['DBHOST'],
            'password': os.environ['DBPASSWORD'],
            'port': os.environ['DBPORT'],
        }
    joined = os.path.join(fs.get_absolute_path(), '../')
    # TODO please add condition checks for other environments
    return json.loads(fs.get_file_contents(joined + f'secrets/{env}.db.json'))

