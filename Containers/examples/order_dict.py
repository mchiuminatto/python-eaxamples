import time
from collections import OrderedDict

# siulate LRU cache

class LRU(OrderedDict):

    def __init__(self, cap):
        super().__init__()
        self.cap = cap

    def get(self, k):
        self.move_to_end(k)
        return self[k]

    def put(self, k, v):
        self[k] = v
        self.move_to_end(k)
        if len(self) > self.cap:
            self.popitem(last=False)  # evict oldest

    def print_me(self):
        time.sleep(2)
        print(list(self), end="\r", flush=True)

c = LRU(2)
c.put("a", 1)
c.print_me()

c.put("b", 2)
c.print_me()

c.get("a")
c.print_me()

c.put("c", 3)
c.print_me()

time.sleep(3)


    