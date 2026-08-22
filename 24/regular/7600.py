from re import *
with open('24_7600.txt') as f:
    data = f.readline()
pattern = r'[^QRS]*([QRS][^QRS]+)+[QRS]?'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))