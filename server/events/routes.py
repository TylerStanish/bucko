from http import HTTPStatus

from flask import Blueprint, request, jsonify

from auth.decorators import require_authentication
from events.db import create_event, get_events_by_user


auth_blueprint = Blueprint('', __name__, url_prefix='/event')


@require_authentication
@auth_blueprint.route('/', methods=['GET'])
def event_get():
    return jsonify({'token': session.token})


@auth_blueprint.route('/', methods=['POST'])
def event_post():
    pass

