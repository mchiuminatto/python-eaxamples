
from time import sleep, time

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took:", time() - t)
    
    return wrapper


@measure
def f(sleep_time):
    sleep(sleep_time)

f(0.5)
