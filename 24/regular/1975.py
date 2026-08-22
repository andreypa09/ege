# data = "P**P**P***P*"
import re

with open('1975.py') as f:
    data = f.readline()
# P***P*P **P** P***P* **P*P
pattern = r"[^P]*(P[^P]+)*P?"
matches = [match.group() for match in re.finditer(pattern, data)]
ans = max(matches, key=len)
print(len(ans))