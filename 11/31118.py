from math import log2, ceil, floor
for N in range(10000, 1, -1):
    i = ceil(log2(N))
    I = ceil(172 * i / 8)
    if I * 187_564 <= 39 * 1024 * 1024:
        print(N)
        break