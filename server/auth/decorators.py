from functools import wraps
from flask import request


def require_authentication(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(request.headers)
        res = f(*args, **kwargs)
        return res
    return wrapper

