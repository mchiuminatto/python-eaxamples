import threading, time

eur, usd = threading.Lock(), threading.Lock()

def trader(first, second, name):
    with first:
        time.sleep(0.1)  # let the other thread grab its lock
        if second.acquire(timeout=1): # a bare acquire would hang for ever
            second.release()
            print(name, "done")
        else:
            print(name, "gave up: deadlock avoided by timeout")

a = threading.Thread(target=trader, args=(eur, usd, "A (EUR-USD)"))
b = threading.Thread(target=trader, args=(usd, eur, "B (USD-EUR)"))

a.start()
b.start()
a.join()
b.join()

