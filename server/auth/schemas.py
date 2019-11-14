from marshmallow import Schema, fields, post_load

from auth.models import Profile


class SignupRequest(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def post_load(self, data, **kwargs):
        return Profile(**data)


class LoginResponse(Schema):
    token = fields.Str()

