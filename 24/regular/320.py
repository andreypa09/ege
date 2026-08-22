import re
with open('24_320.txt') as f:
    data = f.read()
pattern = r"[1-9][0-9]*[02468]"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=lambda x: int(x))
print(answer)