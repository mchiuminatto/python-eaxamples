import math
line = "this is a string"

# string alignment
print(f"{line:<20}")
print(f"{line:>20}")
print(f"{line:^20}")

# Trailing, Front or surround with fill character
number = 999
print(f"{number:0>10}")
print(f"{number:0<10}")
print(f"{number:0^10}")

# group separator
number=12389012
print(f"{number:_}")
print(f"{number:,}")


# decimal precision

print(f"{math.pi:.4}")
print(f"{math.pi:.8}")


