from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool
import time

ITEMS: int  = 100_000
CORES: int = 8

def double(x):
    return 2 * x

if __name__ == "__main__":

    t0 = time.perf_counter() 
    c0 = time.process_time()

    # Option 1: The modern API used in most of this module
    l1 = []
    with ProcessPoolExecutor(max_workers=CORES) as pool:
        l1 = (list(pool.map(double, range(ITEMS), chunksize=2)))

    print("\n------- Option 1 : New API with ProcessPoolExecutor -----")
    print("Elements processed", len(l1))
    print(f"Wall time executor = {time.perf_counter() - t0: .4f}s")
    print(f"CPU time executor = {time.process_time() - c0: .4f}s")


    # Option 2:  The older multiprocess API
    t0 = time.perf_counter() 
    c0 = time.process_time()

    with Pool(processes=CORES) as pool:
        l2 = list(pool.map(double, range(ITEMS), chunksize=2))

    print("\n------- Option 2 : Older multiprocess API -----")
    print("Elements processed", len(l2))
    print(f"Wall time multiprocess = {time.perf_counter() - t0: .4f}s")
    print(f"CPU time multiprocess = {time.process_time() - c0: .4f}s")

