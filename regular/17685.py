from re import *
with open('24_17685.txt') as f:
    data = f.readline()
num  = r"(([1-9][0-9]*)|0)"
zero = rf"({num}\*)*0(\*{num})*"
pattern = rf"({zero}\+)*{zero}"
matches = [match.group() for match in finditer(pattern, data)]
ans = max(matches, key=len)
print(len(ans))