from math import log2, ceil, floor
N = 130
i = ceil(log2(N))
ans = floor(5 * 1024 * 1024 * 1024 * 8 / 12_755_226) / i
print(floor(ans))