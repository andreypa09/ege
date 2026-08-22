import re
with open('24_2424.txt') as f:
    data = f.read()
pattern = r"(XYZ)+"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))