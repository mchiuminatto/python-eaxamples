from random import randint
from time import time

N = 1000000

S = "sdfsdfsd"

for i, ch in enumerate(S):
    print(i, ch)

slice_lo = randint(0, N)
slice_hi = randint(slice_lo, N)

A = [randint(1, N) for _ in range(N)]
pfx = [0]*(len(A))

# print(A, "-", len(A))
pfx[0] = A[0]

for i in range(1, len(A)):
    # print(A[i])
    pfx[i] = pfx[i-1] + A[i]

# print(pfx, "-", len(pfx))
# print(slice_lo, "-", slice_hi)


# calculate slice sum without prefix

t1 = time()
cum_sum = 0
for i in range(slice_lo, slice_hi+1):
    cum_sum += A[i]

print("cum_sum", cum_sum, "time ", time()-t1)

# calculate slice sum with prefix
t1 = time()
cum_sum = pfx[slice_hi] - pfx[slice_lo-1]
print("cum_sum", cum_sum, "time ", time()-t1)





