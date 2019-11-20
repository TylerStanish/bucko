import secrets

from flask import g
import psycopg2

from events.models import Event


def create_event(event: Event, profile_id: str) -> Event:
    cur = g.db.cursor()
    cur.execute("""
        insert into event (
            profile_id,
            event_start,
            event_end,
            title
        ) values (%s, %s, %s, %s) returning *
    """, (profile_id, event.event_start, event.event_end, event.title))
    row = cur.fetchone()
    g.db.commit()
    return row

def get_events_by_profile_id(profile_id: str) -> Event:
    cur = g.db.cursor()
    cur.execute("""
        select * from event where profile_id = %s
    """, (profile_id,))
    row = cur.fetchall()
    g.db.commit()
    return row

