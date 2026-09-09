from math import ceil, log2, floor
N = 512
i = ceil(log2(N))
I = ceil(213 * 1024 / 708 * 8)
L = ceil(I / i)
print(L)


