from re import *
with open('24_27777.txt') as f:
    data = f.readline()
pattern = r'[1-9A-B][0-9A-B]*'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))