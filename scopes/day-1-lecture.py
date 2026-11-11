# Names, namespaces and the LEGB chain 

quotes =  [1.0801, 1.0812]
snapshot = quotes
snapshot.append(1.0797)

print("quotes", quotes, id(quotes))
print("snapshot", snapshot, id(snapshot))
print(snapshot is quotes)

snapshot = [0.0]

print("quotes", quotes, id(quotes))
print("snapshot", snapshot, id(snapshot))
print(snapshot is quotes)


import builtins
import sys


PIP = 0.001
print(globals()["PIP"])
print(globals() is sys.modules[__name__].__dict__)
print("round" in vars(builtins), "round" in globals())
globals()["SPREAD"] = 0.00012
print(SPREAD)


print(" ")
print("-" * 6, "shadowing", "-"*6)

prices = [1.0801, 1.0812, 1.0797]
max = max(prices)
print("max", max)

try:
    print(max([1, 2]))
except TypeError as exc:
    print("Type Error", exc)

del max
try:
    print(max([1, 2]))
except NameError as exc:
    print("Name Error", exc)

"""
What creates scopes:


- modules (G)
- functions (L, E)
- class methods (functions) (L, E)
- lambdas (L, E)
- comprehensions (L)
- class bodies (L)

"""


# blocks don't create scope

for symbol in ["EURUSD", "GBPUSD"]:
    last_seen = symbol
print(symbol, last_seen)

if True:
    risk = 0.01

print(risk)

squares = [n * n for n in range(3)]

try:
    print(n)
except NameError as exc:
    print("NameError", exc)

