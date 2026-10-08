import hashlib, os, time, threading

def countdown(n: int):
    while n:
        n -= 1

def timed(label, target, args, n_threads):
    t0 = time.perf_counter()
    ts = [threading.Thread(target=target, args=args) for _ in range(n_threads)]
    for t in ts: t.start()
    for t in ts: t.join()

    print(f"{label:<28} {time.perf_counter() - t0: .2f}s")


# N = 10_000_000
N = 10
timed("CPU, 1 thread x 2 jobs", lambda: (countdown(N), countdown(N)), (), 1)
timed("CPU, 2 threads x 1 job", countdown, (N,), 2)
timed("sleep 0.5s, 1 thread x 4", lambda: [time.sleep(0.5) for _ in range(4)], (), 1)
timed("sleep 0.5s, 4 threads", time.sleep, (0.5,), 4)
blob = os.urandom(200_000_000)
timed("sha256 200MB, 1 thread x 2", lambda: (hashlib.sha256(blob).digest(), hashlib.sha256(blob).digest()), (), 1)
timed("sha256 200MB, 2 threads", lambda: hashlib.sha256(blob).digest(), (), 2)