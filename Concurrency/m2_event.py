# clean shutdown with event

import threading, time

stop = threading.Event()

def heartbeat():
    beats = 0
    while not stop.wait(timeout=0.1):  # sleeps but wakes instatnly on set()
        beats += 1
    print(f"heartbeat stopped cleanly after {beats} beats")

t = threading.Thread(target=heartbeat)
t.start()
print("Sleeping")
time.sleep(2)
stop.set()
t.join()


