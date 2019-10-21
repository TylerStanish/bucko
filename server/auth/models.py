from collections import namedtuple

fields = (
    'id',
    'email',
    'password'
)
Profile = namedtuple('Profile', fields, defaults=(None,) * len(fields))

fields = (
    'id',
    'token',
    'profile_id'
)
AuthSession  = namedtuple('AuthSession', fields, defaults=(None,) * len(fields))
