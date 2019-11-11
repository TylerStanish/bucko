from http import HTTPStatus

from flask import Blueprint, request, jsonify

from auth.decorators import require_authentication
from auth.models import Profile
from events.db import create_event, get_events_by_profile_id
from events.schemas import EventSchema


events_blueprint = Blueprint('events', __name__, url_prefix='/event')


@events_blueprint.route('/', methods=['GET'])
@require_authentication
def event_get(profile: Profile):
    events = get_events_by_profile_id(profile.id)
    return jsonify(EventSchema(many=True).dump(events))


@events_blueprint.route('/', methods=['POST'])
@require_authentication
def event_post(profile):
    data: Event = EventSchema().load(request.get_json())
    event = create_event(data, profile.id)
    return jsonify(EventSchema().dump(event))

