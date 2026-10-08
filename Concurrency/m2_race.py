import sys, threading

sys.setswitchinterval(1e-6)  # time a thread (holding the GIL) have to release the GIL to another wating thread.

balance = {"EUR": 0}
lock = threading.Lock()  # generates a mutex

def fee(amount):  # every call betweent read and write is a switch point
    return amount

def deposit_unsafe(n):
    print (f"Unsafe {n}, ", end="")
    for _ in range(n):
        current = balance["EUR"]  # read
        balance["EUR"] = current + fee(1)  # modify

def deposit_safe(n):
    print(f"Safe {n}, ", end="")
    for _ in range(n):
        with lock:  # mutex lock
            current = balance["EUR"]  # read
            balance["EUR"] = current + fee(1)  # modify


for fn in (deposit_unsafe, deposit_safe):
    balance["EUR"] = 0
    ts =  [threading.Thread(target=fn, args=(200_000, )) for _ in range(4)]
    for t in ts: t.start()
    for t in ts: t.join()

    print(f"{fn.__name__ : <15} expected 800.000, got {balance["EUR"]}")
