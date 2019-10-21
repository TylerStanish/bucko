from flask import g

import psycopg2

from auth.models import Profile


def create_user(profile: Profile) -> Profile:
    cur = g.db.cursor()
    # TODO please convert this to a server-side db function?
    cur.execute("""
        insert into profile (email, hashed_password) values (%s, %s) returning *
    """, profile.email, profile.hashed_password)
    row_dict = cur.fetchone()
    g.db.commit()
    return Profile(**row_dict)

