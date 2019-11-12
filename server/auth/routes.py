from http import HTTPStatus

from flask import Blueprint, request, jsonify

from auth.db import create_user, create_user_session
from auth.exceptions import ApiException, IncorrectPasswordException
from auth.models import Profile
from auth.schemas import SignupRequest, LoginResponse
from auth.services import check_password_matches, hash_password, valid_login


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data: Profile = SignupRequest().load(request.get_json())
    data = data._replace(password=hash_password(data.password))
    profile = create_user(data)
    session = create_user_session(profile)
    return jsonify({'token': session.token})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data: Profile = SignupRequest().load(request.get_json())
    valid, profile = valid_login(data.email, data.password)
    if not valid:
        raise ApiException('Incorrect password', HTTPStatus.BAD_REQUEST )
    session = create_user_session(profile)
    return jsonify({'token': session.token})

