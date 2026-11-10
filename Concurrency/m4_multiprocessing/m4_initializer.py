import os
import time

from concurrent.futures import ProcessPoolExecutor

_history = None  # one copy per worker


def load_history():
    global _history  # avoids shadowing global _history
    time.sleep(0.2)
    _history = list(range(1_000_000))
    print(f"worker {os.getpid()} loaded history")

def score(window):
    return window, sum(_history[::window]) % 10000

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2, initializer=load_history) as pool:
         for window, s in pool.map(score, range(1, 9)):
            print(f"windows={window}  score={s}")





