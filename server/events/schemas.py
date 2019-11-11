from marshmallow import Schema, fields

from events.models import Event


class EventSchema(Schema):
    id = fields.Str(dump_only=True)
    profile_id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    start = fields.DateTime(required=True)
    end = fields.DateTime(required=True)

    @post_load
    def post_load(self, data, **kwargs):
        return Event(**data)

