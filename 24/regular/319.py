import re
with open('24_319.txt') as f:
    data = f.read()
pattern = r"[1-9][0-9]*[13579]"
matches = [match.group() for match in re.finditer(pattern, data)]
print(matches)
answer = min(matches, key=lambda x: int(x))
print(answer)