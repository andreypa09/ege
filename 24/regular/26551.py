from re import *
with open("24_26551.txt") as f:
    data = f.readline()
# data = "1234ABC837450AB"
pattern = r"[1-9A-D][0-9A-D]*[02468AC]"
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))
