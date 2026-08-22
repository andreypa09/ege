from re import *
with open('24_22356.txt') as f:
    data = f.readline()
pattern = r'[1-9A-B][0-9A-B]*[13579B]'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=lambda x: int(x, 12))
print(data.find(answer))