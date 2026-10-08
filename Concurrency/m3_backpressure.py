"""

What to notice: the producer could generate all 8 items instantly, 
but the consumer needs 0.1 s per item and the queue holds only 3. 
The first 4 puts are instant: items 0–2 fill the queue and the consumer has already taken one off, 
freeing a slot. From item 4 on, every put() waits about 0.1 s, exactly one consumer step, so the 
producer is automatically slowed to the consumer's speed. With an unbounded queue all 8 puts would 
show 0.00 s and the items would just pile up in memory. At the end, STOP is the sentinel that tells 
the consumer to exit its loop, and q.join() returns only after every item, the sentinel included, 
has been marked task_done().

"""

import queue, threading, time

q = queue.Queue(maxsize=3)
STOP = object()

def producer():
    for i in range(8):
        t0 = time.perf_counter()
        q.put(i)
        waited = time.perf_counter() - t0
        print(f"put {i} (blocked {waited: 2f}s)")
    q.put(STOP)

def consumer():
    while (item:= q.get()) is not STOP:
        time.sleep(0.1)  # slows down consumer
        q.task_done()
    q.task_done()


threading.Thread(target=consumer).start()
producer()
q.join()  #  every put matched by a task done

print ("All items processed")


