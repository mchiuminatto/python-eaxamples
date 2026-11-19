import time
def profile(fn, *args):
    w0 = time.perf_counter()  # stop watch to measure the duration of a process
    c0 = time.process_time()  # measures the effective processing time, not necessarily the duration.

    fn(*args)

    wall = time.perf_counter() - w0
    cpu = time.process_time() - c0

    print(f"{fn.__name__:<8} wall={wall: 2f}s cpu={cpu: 2f}s cpu/wall = {cpu/wall: 0%}")



def crunch(n: int):  # pure python aruthmetic
    return sum(i * i for i in range(n))


def wait(seconds: int):
    time.sleep(seconds)



print("------ Example 1 ------------------")
profile(crunch, 5_000_000)  # pure cpu time
profile(wait, 2)  # pure wait time


# /home/mchiuminatto/work/dev/tradig-strategy-research/data/raw/GBPJPY_5 Mins_Ask_2014.09.01_2026.09.01.parquet
# /home/mchiuminatto/work/dev/tradig-strategy-research/data/raw/GBPJPY_5 Mins_Bid_2014.09.01_2026.09.01.parquet




