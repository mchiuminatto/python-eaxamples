


xs = [10, 20, 30, 40, 50]
print(xs[-1])  # last one
print(xs[:2], xs[0:2])  # first 2
print(xs[::2])  # each two items starting from 0
print(xs[::-1])  # reverse
print(xs[::-2])  # reverse with step 2
print(id(xs))
xs = xs + [60]  # concatenates in a new list
print(xs)
print(id(xs))
xs += [70]  # extends the current list
print("-" * 6, "extend", "-" * 6)
xs.extend([80])
print(xs)
print(id(xs))
first, *rest = xs
print("first", first)
print("rest", rest)
