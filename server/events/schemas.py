from marshmallow import Schema, fields, post_load

from events.models import Event


class EventSchema(Schema):
    id = fields.Str(dump_only=True)
    profile_id = fields.Str(dump_only=True, data_key='profileId')
    title = fields.Str(required=True)
    event_start = fields.DateTime(required=True, data_key='eventStart')
    event_end = fields.DateTime(required=True, data_key='eventEnd')

    @post_load
    def post_load(self, data, **kwargs):
        return Event(**data)

