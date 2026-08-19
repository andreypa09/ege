from re import *
with open('24.23_19887.txt') as f:
    data = f.readline()
pattern = r'[13579]?([02468][13579])+[02468]?'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key = len)
print(len(answer))