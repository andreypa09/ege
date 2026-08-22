import re
with open('24_865.txt') as f:
    data = f.readline()
pattern = r"[^CF]+"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))