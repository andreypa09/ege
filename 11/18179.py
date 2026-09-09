from math import log2, ceil, floor
I = ceil(11 * 1024 * 1024 * 8 / 600000)
i = ceil(I / 20)
N = (2**(i-1))+1
print(N)