import re
with open('24_3792.txt') as f:
    data = f.readline()
pattern = r"([ABC])+"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))