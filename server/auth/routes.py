from flask import Blueprint

from auth.db import create_user
from auth.models import Profile


auth_blueprint = Blueprint('', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    profile = Profile(email='tystanish@gmail.com', hashed_password='$jLKioahbioa$')
    profile = create_user(profile)
    return profile._asdict()


@auth_blueprint.route('/login', methods=['POST'])
def login():
    return 'hi'

