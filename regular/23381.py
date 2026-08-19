from re import *
from string import ascii_uppercase
with open('24_23381.txt') as f:
    data = f.readline()
###
# m = 0
# for i in ascii_uppercase:
#     pattern = fr'[02468]{i}+[02468]'
#     matches = [match.group() for match in finditer(pattern, data)]
#     if matches:
#
#         m = max(m, len(max(matches, key=len)))
# print(m)
###
m = 0
pattern = fr'[02468][A-Z]+[02468]'
matches = [match.group() for match in finditer(pattern, data)]
for match in matches:
    if len(set(match[1:-1])) == 1:
        m = max(m, len(match))
print(m)
###
pattern = fr'[02468]([A-Z])\1+[02468]'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))