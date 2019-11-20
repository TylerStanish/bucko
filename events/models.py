from collections import namedtuple

event_fields = (
    'id',
    'profile_id',
    'title',
    'event_start',
    'event_end'
)
Event = namedtuple(
    'Event',
    event_fields,
    defaults=(None,) * len(event_fields)
)
