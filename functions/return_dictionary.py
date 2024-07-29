import random

def build_local_dict():
    d1 = {"number": random.randint(-100, 100)}
    print("Function scope ", id(d1))
    return d1

l1 = []
for i in range(10):
    d1 =  build_local_dict()
    print("Outside scope", id(d1))
    l1.append(d1)

print(l1)
