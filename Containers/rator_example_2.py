# Generator Example (Using Function)
def count(low, high):
    while low <= high:
        yield low
        low += 1

# Using the Generator
gen = count(1, 3)
for num in gen:
    print(num)


next(gen)