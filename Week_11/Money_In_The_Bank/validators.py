import hashlib
import uuid
from settings import *
from functools import wraps
import re
import sql_manager


def command_valitation(*commands):
    def wrapper(func):
        @wraps(func)
        def cheker(arg):
            if arg not in commands:
                raise AssertionError(NOT_VALID_MESSAGE)
            else:
                return func(arg)
        return cheker
    return wrapper


def validate_pass():
    def wrapper(func):
        @wraps(func)
        def cheker(ps):
            pattern = PASS_REG
            result = re.match(pattern, ps)
            if not result:
                raise ValueError(WRONG_VALUE)
            else:
                return ps
        return cheker
    return wrapper


def encrypt_pass():
    def wrapper(func):
        @wraps(func)
        def cheker(password):
            salt = uuid.uuid4().hex
            hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
            return hashed_pass
        return cheker
    return wrapper


def verify_user():
    def wrapper(func):
        @wraps(func)
        def cheker(username, password):
            user = sql_manager.get_user(username)
            if not user:
                raise ValueError("No such user in system")
            salt = uuid.uuid4().hex
            hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
            if hashed_pass != user.password:
                raise ValueError(WRONG_VALUE)
            return user
        return cheker
    return wrapper
