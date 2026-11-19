"""
An object is hashable when: 
    - it has a hash value that never changes during its lifetime and 
    - it can be compared with __eq__. 
The rule that matters is one-directional: if a == b then hash(a) == hash(b). 
Unequal objects may share a hash; that is called a collision and is legal.
"""

print(hash(42), hash((1, "EURUSD")) == hash((1, "EURUSD")))

# Equal objects MUST have equal hashes, across types:

print(1 == 1.0 == True, hash(1)==hash(1.0)==hash(True))

# hashable - non hashable objects

for candidate in ([1, 2], {"a": 1}, {1, 2}, (1, [2])):
    try:
        hash(candidate)
    except TypeError as exc:
        print(type(candidate).__name__, "->", exc)

class Order:  # default: identity-based __eq__ and __hash__
    def __init__(self, oid):
        self.oid = oid

class OrderByValue:  # defining __eq___ sets __hash__ to None
    def __init__(self, oid):
        self.oid = oid

    def __eq__(self, other):
        return self.oid == other.oid

    a = Order(1)
    b = Order(1)
    print(f"id(a): {id(a)}, id(b): {id(b)}")  # two objects two identities
    print(f"hash(a): {hash(a)}, hash(b) {hash(b)}") 
    print(f"hash(a)==hash(b): {hash(a)==hash(b)}")  



