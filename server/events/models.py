from collections import namedtuple

event_fields = (
    'id',
    'profile_id',
    'title',
    'start',
    'end'
)
Event = namedtuple(
    'Event',
    profile_fields,
    defaults=(None,) * len(profile_fields)
)
