def fn(a, b, c=[]):
    c.append(a+b)
    return a+b, c

print(fn(1,1))
print(fn(1,1))
print(fn(1,1))
print(fn(1,1))

print(fn.__defaults__)