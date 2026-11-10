# using queues
from collections import deque

q1 = deque()  #creates an empty queue
print("empty queue", q1)
q1.append("USD")
print(q1)

print("empty queue", q1)
queue = deque(["USDJPY", "EURUSD", "GBPUSD"])
print(queue)
queue.append ("AUDUSD")
print(queue)
queue.appendleft("USDOLLAR")
print(queue)
print(queue.popleft())
print(queue)
q2 = queue.copy()
print("q2", q2)
print(q2.pop())
print("q2", q2)




