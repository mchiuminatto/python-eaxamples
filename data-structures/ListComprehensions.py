# using list comprehensions
squares = {x**2 for x in range(10)}
print(squares)
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)
I3 = [(x, y, z) for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3] if ((x == y) and (y == z))]
print(I3)


# using nested comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("unpacked", *matrix)

T = [[row[i] for row in matrix] for i in range(4)]
print(T)
