import re
with open('24_2419.txt') as f:
    data = f.readline()
pattern = r"C*"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))