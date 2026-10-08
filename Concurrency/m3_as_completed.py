import random, time, datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


def quote(pair):
    time.sleep(random.uniform(1, 2))  # random sleep
    if pair == "USD/XXX":
        raise LookupError(f"Unknown pair {pair}")
    return pair, round(random.uniform(1, 2), 4),datetime.datetime.now().strftime("%H:%M:%S.%s")

pairs = ["EUR/USD", "GBP/USD", "USD/XXX", "AUD/USD"]
random.seed(7)

with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(quote, p): p for p in pairs}  # submit each task to a thread in te pool, the object function is the key
    for fut in as_completed(futures, timeout=2): #  the iterator yields a future as its task is completed
        pair = futures[fut]
        try:
            print("ok ", fut.result())
        except LookupError as exc:
            print("Error ", pair, "--> ", exc)

