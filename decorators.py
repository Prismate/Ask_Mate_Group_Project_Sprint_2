# DECORATORS
# https://www.youtube.com/watch?v=FsAPt_9Bf3U
import time
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{__file__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran {orig_func.__name__} with args: {args}, and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2}")
        return result

    return wrapper


def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"wrapper executed this before {original_function.__name__} at {time_string}")
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"call method executed this before {self.original_function.__name__} at {time_string}")
        return self.original_function(*args, **kwargs)


@decorator_function
@my_timer
@my_logger
def display():
    print('display function ran')


# line below is the same functionality as decorator code above
# display = decorator_function(display)


@decorator_function
@my_logger
@my_timer
def sum_numbers(*args: int, **kwargs):
    res = 0
    for arg in args:
        res += arg
    return res


# display()
print(sum_numbers(1, 2, 3, 4, 5, 6, 7))
