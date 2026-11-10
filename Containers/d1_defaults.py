"""
Python passes references to functions, so a function that mutates an argument mutates the caller's object. 
This is called `call by sharing`. 
Default argument values are evaluated once, when the def statement runs, and live on the function object in __defaults__.
"""


# Default values are evaluated ONCE, when 'def' runs, and stored on the function.
def add_fill(qty, fills=[]):
    fills.append(qty)
    return fills

print(add_fill(100))
print(add_fill(200))            # same list object as the first call
print(add_fill.__defaults__)

def add_fill_safe(qty, fills=None):
    if fills is None:           # sentinel: build a fresh list per call
        fills = []
    fills.append(qty)
    return fills

print(add_fill_safe(100), add_fill_safe(200))