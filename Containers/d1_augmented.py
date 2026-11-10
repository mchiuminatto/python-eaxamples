# Augmented assignment <v1> += <v2 | value>  mutates if possible the rebinds

print()
print("Collections augmented assignment")

a = [1, 2]
b = a
a += [3]  # list.__iadd__ mutates in place and returns the same object
print(a, b, a is b)

t = (1, 2, 3)
u = t
t += (3, )  # tuple has no __iadd__: falls back to t = t + (3) new tuple
print(t, u, t is u)

ticket = ("EURUSD", [100_000])
try:
    ticket[1] += [50_000]  # list mutates, thenm tuple assignmnt fails (tuples are immutable)
except TypeError as exc:
    print("TypeError: ", exc)

print(ticket)  # the inner list was changed anyways
