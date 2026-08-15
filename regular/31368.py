# 0+0+756*0
from re import *
with open('24_31368.txt') as f:
    data = f.readline()
# data = "0++53631*71182+3710*+*0+0+0+0+73819*0++0*0*0*46791*0++0+83287*0+0++0*0+0+0+0+0+0*0**0+91372+0*58428+0+0+0*0*0+0+0*0*0*+*0*0*0+0*0"
num  = r"(([1-9][0-9]*)|0)"
zero = rf"({num}\*)*0(\*{num})*"
pattern = rf"({zero}\+)*{zero}"
matches = [match.group() for match in finditer(pattern, data)]

ans = max(matches, key=len)

print(len(ans))