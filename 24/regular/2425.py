import re
with open('24_2425.txt') as f:
    data = f.readline()
pattern = r"(DBAC)*((DBA)|(DB)|(D))?"
matches = [match.group() for match in re.finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))