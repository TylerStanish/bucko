import secrets

from flask import g
import psycopg2

from auth.models import AuthSession, Profile


def create_event(event: Event) -> Event:
    cur = g.db.cursor()
    cur.execute("""
        insert into event (profile_id, start, end, title) values (%s, %s) returning *
    """, (event.profile_id, event.start, event.end, event.title))
    row = cur.fetchone()
    g.db.commit()
    return row

def get_events_by_profile_id(profile_id: str) -> Event:
    cur = g.db.cursor()
    cur.execute("""
        select * from event where profile_id = %s
    """, (email,))
    row = cur.fetchone()
    g.db.commit()
    return row

