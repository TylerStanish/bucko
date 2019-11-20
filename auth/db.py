import secrets

from flask import g
import psycopg2

from auth.models import AuthSession, Profile


def create_user(profile: Profile) -> Profile:
    cur = g.db.cursor()
    # TODO please convert this to a server-side db function?
    cur.execute("""
        insert into profile (email, password) values (%s, %s) returning *
    """, (profile.email, profile.password))
    row = cur.fetchone()
    g.db.commit()
    return row


def create_user_session(profile: Profile):
    cur = g.db.cursor()
    cur.execute("""
        insert into auth_session (token, profile_id) values (%s, %s) returning *
    """, (secrets.token_urlsafe(63), profile.id))
    row = cur.fetchone()
    g.db.commit()
    return row


def get_profile_by_email(email: str) -> Profile:
    cur = g.db.cursor()
    cur.execute("""
        select * from profile where email = %s
    """, (email,))
    row = cur.fetchone()
    g.db.commit()
    return row

def get_profile_by_token(token: str) -> Profile:
    cur = g.db.cursor()
    cur.execute("""
        select
            profile.id,
            email,
            password
        from profile inner join auth_session
            on (profile.id = auth_session.profile_id)
        where auth_session.token = %s
    """, (token,))
    row = cur.fetchone()
    g.db.commit()
    return row
