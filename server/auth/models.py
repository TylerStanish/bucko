from collections import namedtuple

fields = (
    'id',
    'email',
    'hashed_password'
)

Profile = namedtuple('Profile', fields, defaults=(None,) * len(fields))
