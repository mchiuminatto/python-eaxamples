"""
A shallow copy creates a new outer container that holds references to the same inner objects. 
- list(x), 
- x[:], 
- x.copy(), 
- dict(x), 
- {**x} and 
- copy.copy(x) are all shallow. 

copy.deepcopy recurses and keeps a memo dictionary so shared or cyclic references are copied once.
"""

import copy

book = {
    "EURUSD": [100_000, -50_000], 
    "GBPUSD": [25_000]
    }

print("\nStage setting ", flush=True)

shallow = dict(book)
deep = copy.deepcopy(book)

print(f"book : {book}, {id(book)}")
print(f"shallow : {shallow}, {id(shallow)}")
print(f"deep : {deep}, {id(deep)}")

print()
print("Mutating an inner object")
book["GBPUSD"].append(35_000)

print(f"book : {book}, {id(book)}")
print(f"shallow : {shallow}, {id(shallow)}")
print(f"deep : {deep}, {id(deep)}")


print()
print("New key")
book["USDJPY"] = [200_000]


print(f"book : {book}, {id(book)}")
print(f"shallow : {shallow}, {id(shallow)}")
print(f"deep : {deep}, {id(deep)}")

# The classic aliasing trap: the outer list holds 3 references to ONE row.

print()
print("Aliasing ")

grid = [[0]*3]*3  # repeats the row
print(grid)

for i, row in enumerate(grid):
    print(i, row, id(row))

print("After assignment")
grid[0][0] = 9

for i, row in enumerate(grid):
    print(i, row, id(row))


print("How to create different objects for row")
grid = [[0]*3 for _ in range(3)]
grid[0][0] = 9

for i, row in enumerate(grid):
    print(i, row, id(row))


