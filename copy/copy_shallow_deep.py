l1 = [1, 2, 3, {"1":"2"}]
print(l1)
l2s = l1.copy()
print(l2s)
l2s.pop(0)
print("After pop")
print(l1)
print(l2s)

l2s[2]["1"] = 5

print("After modification")
print(l1)
print(l2s)

import copy

l2d = copy.deepcopy(l1)

print("l1", l1)
print("l2s", l2s)
print("l2d", l2d)


l2d[3]["1"] = 10


print("After mew modification")

print("l1", l1)
print("l2s", l2s)
print("l2d", l2d)
