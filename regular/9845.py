import re
from re import *
with open('24_9845.txt') as f:
    data = f.readline()
pattern = r'[89]?([ABC][^ABC])+[ABC]?'
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))