from flask import Blueprint, request, jsonify

from auth.db import create_user, create_user_session
from auth.models import Profile
from auth.schemas import SignupRequest, LoginResponse


auth_blueprint = Blueprint('', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = SignupRequest().load(request.get_json())
    # TODO hash password!
    profile = create_user(data)
    session = create_user_session(profile)
    return jsonify({'token': session.token})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    return 'hi'

