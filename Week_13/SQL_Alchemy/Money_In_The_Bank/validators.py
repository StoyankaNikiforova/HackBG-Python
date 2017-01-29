import hashlib
import uuid
from settings import WRONG_VALUE, NOT_VALID_MESSAGE, PASS_REG
from functools import wraps
import re


def command_valitation(*commands):
    def wrapper(func):
        @wraps(func)
        def cheker(*args):
            if args[0]in commands:
                return func(*args)
            else:
                print(NOT_VALID_MESSAGE)

        return cheker
    return wrapper


def validate_pass(func):
    def cheker(ps):
        pattern = PASS_REG
        result = re.match(pattern, ps)
        if result:
            return func(ps)
        else:
            raise ValueError(WRONG_VALUE)
    return cheker


def encrypt_pass(func):
    def cheker(password):
        salt = uuid.uuid4().hex
        hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return func(hashed_pass)
    return cheker


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
