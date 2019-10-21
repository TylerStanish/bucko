from flask import Blueprint, request

from auth.db import create_user
from auth.models import Profile
from auth.schemas import SignupRequest, LoginResponse


auth_blueprint = Blueprint('', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = SignupRequest().load(request.get_json())
    # TODO hash password!
    profile = create_user(data)
    return profile._asdict()


@auth_blueprint.route('/login', methods=['POST'])
def login():
    return 'hi'

