from functools import wraps
from http import HTTPStatus

from flask import request

from auth.db import get_profile_by_token
from auth.exceptions import ApiException


def require_authentication(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            raise ApiException('Token not provided', HTTPStatus.UNAUTHORIZED)
        spl = auth.split(' ')
        if len(spl) < 2:
            raise ApiException('Invalid token', HTTPStatus.UNAUTHORIZED)
        tok = auth.split(' ')[1]
        profile = get_profile_by_token(tok)
        if not profile:
            raise ApiException('Token does not exist', HTTPStatus.UNAUTHORIZED)
        res = f(profile, *args, **kwargs)
        return res
    return wrapper

