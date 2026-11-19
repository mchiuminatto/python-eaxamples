import time
from concurrent.futures import ProcessPoolExecutor


def backtest(window):
    total = 0
    for i in range(3_000_000):
        total += (i % window) * (i % 7)
    return window, total

if __name__ == "__main__":
    windows = [5, 10, 20, 40]

    # ------ serial execution -----
    t0 = time.perf_counter()
    serial = [backtest(w) for w in windows]
    print(f"serial     {time.perf_counter() - t0: .2f}s")
    t0 = time.perf_counter()


    # ---- paralle execution ------
    with ProcessPoolExecutor(max_workers=2) as pool:
        parallel = list(pool.map(backtest, windows))

    print(f" 2 processes   {time.perf_counter() - t0: .2f}s")

    assert parallel == serial





