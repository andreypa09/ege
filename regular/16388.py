from re import *
with open('24_16388.txt') as f:
    data = f.readline()
# data = "MNKLMNKLMNKLMNKLM"
pattern = r"[(LMN)(MN)(N)](KLMN)*[(KLM)(KL)(K)]"
mathes = [match.group() for match in finditer(pattern, data)]
ans = max(mathes, key=len)
print(len(ans))