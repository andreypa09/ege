import re
from re import *
with open('24_31129.txt') as f:
    data = f.readline()
# data = "123-3123*0-231*0-0-0"
num = r"(([1-4][0-4]*)|0)"
pattern = rf"({num}[-*])+{num}"
matches = [match.group() for match in finditer(pattern, data)]
ans = max(matches, key=len)
print(len(ans))