from collections import deque
import time

# dequeue rolling windows
window = deque(maxlen=3)

for px in [1.0841, 1.0843, 1.0840, 1.0846, 1.0754]:
    window.appendleft(px) # older falls off
    print(window, end="\r", flush=True)
    time.sleep(0.5)
print("/n")
print(list(window))
