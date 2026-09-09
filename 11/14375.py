from math import ceil, log2, floor
N = 62
i = ceil(log2(N))
ans = floor(20 * 1024 / ceil(23 * i / 8 + 10))
print(ans)