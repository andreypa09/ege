from math import log2, ceil, floor
N = 25 + 487
i = ceil(log2(N))
I = ceil(70 * 1024 * 8/ 345)
L = ceil(I / i)
print(L)