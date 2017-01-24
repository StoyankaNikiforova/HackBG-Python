from settings import *
from functools import wraps
import re


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


# def validate_pass(password):
#     pattern = PASS_REG
#     result = re.match(pattern, password)
#     if not result:
#         raise ValueError(WRONG_VALUE)
#     else:
#         return password

# def encrypt_pass():
    # def wrapper(func):
    #     @wraps(func)
    #     def cheker(arg):
    #         pass
    #     return cheker
    # return wrapper
    #





def verify_pass(*commands):
    def wrapper(func):
        # @wraps
        def cheker(arg):
            if arg not in commands:
                pass
        return cheker
    return wrapper
