# decorators/time.measure.start.py
from time import sleep, time

def f(sleep_time=0.3):
    sleep(sleep_time)



def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took:", time() - t)

measure(f, 0.5)
measure(f, 0.3)