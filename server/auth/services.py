import bcrypt

from auth.db import get_profile_by_email


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password_matches(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def valid_login(email: str, password: str) -> bool:
    profile = get_profile_by_email(email)
    if profile is None:
        return False, None
    return check_password_matches(password, profile.password), profile

