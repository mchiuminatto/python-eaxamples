from time import sleep, time
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, func.__doc__, "took:", time() - t)
    return wrapper


@measure
def f(sleep_time):
    """
    Sleeping time, zzzz
    """
    sleep(sleep_time)

f(0.5)
print(">>>>", f.__name__, f.__doc__ )