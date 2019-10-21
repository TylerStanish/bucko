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
    row_dict = cur.fetchone()
    g.db.commit()
    return Profile(**row_dict)


def create_user_session(profile: Profile):
    cur = g.db.cursor()
    cur.execute("""
        insert into auth_session (token, profile_id) values (%s, %s) returning *
    """, (secrets.token_urlsafe(63), profile.id))
    row_dict = cur.fetchone()
    g.db.commit()
    return AuthSession(**row_dict)

