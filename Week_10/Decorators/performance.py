import time
from functools import wraps


def performance(file_name):
    def perf_of_func(func):
        import logging
        logging.basicConfig(filename=file_name, level=logging.INFO)

        @wraps(func)
        def writer():
            start_time = time.time()
            result = func()
            time_diff = time.time() - start_time
            logging.info("{} was called and took {:.2} seconds to complete".format(func.__name__, time_diff))
            return result
        return writer
    return perf_of_func


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


def main():
    print(something_heavy())


if __name__ == '__main__':
    main()
