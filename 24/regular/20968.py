from re import *
with open('24_20968.txt') as f:
    data = f.readline()
num = r"(([1-9][0-9]*[02468])|[02468])"
pattern = rf"({num}[+*])+{num}"
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))