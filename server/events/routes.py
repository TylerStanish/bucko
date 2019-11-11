from http import HTTPStatus

from flask import Blueprint, request, jsonify

from auth.decorators import require_authentication
from events.db import create_event, get_events_by_profile_id


events_blueprint = Blueprint('events', __name__, url_prefix='/event')


@events_blueprint.route('/', methods=['GET'])
@require_authentication
def event_get():
    return jsonify([])


@events_blueprint.route('/', methods=['POST'])
def event_post():
    pass

