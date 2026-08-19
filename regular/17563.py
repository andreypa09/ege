from re import *
with open('24_17563.txt') as f:
    data = f.readline()
num = r'[789][0789]*'
pattern = rf'({num}[-*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches,key=len)
print(len(answer))