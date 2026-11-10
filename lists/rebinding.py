a = [1, 2]
b = a
a += [3]  # expand on the same object
print(id(b), id(a), b)  # [1, 2, 3]

x = [1, 2]
y = x  
x = x + [3] # creates a new object
print(id(x), id(y), y)  # [1, 2]  