from functools import wraps
from settings import NOT_VALID_MESSAGE


def command_valitation(*commands):
    def wrapper(func):
        @wraps
        def cheker(arg):
            if arg not in commands:
                raise AssertionError(NOT_VALID_MESSAGE)
            else:
                return func(arg)
        return cheker
    return wrapper


def validate_pass(*commands):
    def wrapper(func):
        @wraps
        def cheker(arg):
            pass
        return cheker
    return wrapper


def verify_pass(*commands):
    def wrapper(func):
        @wraps
        def cheker(arg):
            if arg not in commands:
                pass
        return cheker
    return wrapper
