from collections import namedtuple

profile_fields = (
    'id',
    'email',
    'password'
)
Profile = namedtuple(
    'Profile',
    profile_fields,
    defaults=(None,) * len(fields)
)

auth_session_fields = (
    'id',
    'token',
    'profile_id'
)
AuthSession  = namedtuple(
    'AuthSession',
    auth_session_fields,
    defaults=(None,) * len(fields)
)
