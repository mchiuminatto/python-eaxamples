"""
Exceptions vs dead worker
"""

import os
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool  # error class to capture due to process stop working

def risky(x):
    if x == 3:
        raise ValueError(f"bad tick in file {x}")
    if x == 5:
        os._exit(1)  # ends the process with exit code 1, skips al regular exit protocol
    return x * 10


if __name__  == "__main__":

    # this captures a ValueError Exception from the worker
    with ProcessPoolExecutor(max_workers=2) as pool: 
        futures = {x: pool.submit(risky, x) for x in range(1, 4)}
        for x, fut in futures.items():
            try:
                print(x, "->", fut.result())
            except ValueError as exc:
                print(x, "-> ValueError:", exc)


    # this make the worker exit immediately
    with ProcessPoolExecutor(max_workers=2) as pool:
        try:
            print(list(pool.map(risky, [4, 5, 6])))
        except BrokenProcessPool as exc:
            print("BrokenProcessPool --> ", exc)


