import time 
from multiprocessing import Pool

def tiny(x):
    return x*x

if __name__ == "__main__":
    data = range(200_000)
    with Pool(processes=2) as pool:
        for chunk in (1, 100, 5_000):
            t0 = time.perf_counter()
            pool.map(tiny, data, chunksize=chunk)
            print(f"chunksize = {chunk:<6} {time.perf_counter() - t0: .2f}s")

    data_s = range(200_000)
    t0 = time.perf_counter()
    [tiny(x) for x in data]
    print(f"plain loop    {time.perf_counter() - t0: .2f}s")




