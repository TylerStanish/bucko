from flask import Blueprint, request, jsonify

from auth.db import create_user, create_user_session, check_user_login
from auth.models import Profile
from auth.schemas import SignupRequest, LoginResponse
from auth.services import check_password_matches, hash_password, valid_login


auth_blueprint = Blueprint('', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data: Profile = SignupRequest().load(request.get_json())
    # TODO hash password!
    profile = create_user(data)
    session = create_user_session(profile)
    return jsonify({'token': session.token})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data: Profile = SignupRequest().load(request.get_json())
    if not valid_login(data.email, data.password):
        raise IncorrectPasswordException
    profile = check_user_login(data)
    session = create_user_session(profile)
    return jsonify({'token': session.token})

