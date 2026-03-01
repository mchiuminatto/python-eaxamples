import heapq


h1 = [1, 10, 5, 3, 20, 15]

heapq.heapify(h1)

print("smallest", heapq.heappop(h1))
print("smallest", heapq.heappop(h1))
print("smallest", heapq.heappop(h1))
heapq.heappush(h1, 2)
print("smallest", heapq.heappop(h1))


