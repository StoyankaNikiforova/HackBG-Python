from functools import wraps
from encrypt_decorator import encrypt
import datetime


def log(file_name):
    def loged_func(func):
        import logging
        logging.basicConfig(filename=file_name, level=logging.INFO)

        @wraps(func)
        def writer():
            import time
            logging.info("{} was called at {}".format(func.__name__, datetime.datetime.now()))
            return func()
        return writer
    return loged_func


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


def main():
    print(get_low())

if __name__ == '__main__':
    main()
