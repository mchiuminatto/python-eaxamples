from collections import namedtuple

#  light immutable record

Tick = namedtuple("Tick", "symbol bid ask")
t = Tick("EURUSD", 1.0841, 1.0843)
print(t)
print("Spread", round(t.ask - t.bid, 4))
print(t._replace(bid=1.0842))

