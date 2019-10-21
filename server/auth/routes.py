from flask import Blueprint

from auth.db import create_user


auth_blueprint = Blueprint('', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    profile = create_user()
    # TODO serialize
    return profile


@auth_blueprint.route('/login', methods=['POST'])
def login():
    return 'hi'

