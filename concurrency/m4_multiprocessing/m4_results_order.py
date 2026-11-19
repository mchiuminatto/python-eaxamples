import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def fit(pair, seconds):
    print(pair, seconds)
    time.sleep(seconds)
    return pair


jobs = {
    "EURUSD": 0.6,
    "GBPUSD": 0.2,
    "USDJPY": 0.4,
    "AUDUSD":0.1
        }

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as pool:  # starts 4 pool, executor workers

        # this returns in order
        print("------ returns in input order so needs to wait for all to finish ----")
        t0 = time.perf_counter()
        for pair in pool.map(fit, jobs, jobs.values()):
            print(f"map   {pair} at {time.perf_counter() - t0: 0.2f}s")


        # this return as soon a s finished
        print("-------- returns in as soon as possible order ------")
        t0 = time.perf_counter()
        futures = [pool.submit(fit, p, s) for p, s in jobs.items()]
        for fut in as_completed(futures):
            print(f"as_completed {fut.result()}  at {time.perf_counter() - t0: 0.2f}s")


