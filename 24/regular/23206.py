from re import *
with open('24_23206.txt') as f:
    data = f.readline()
pattern = r'[02468][^02468S]*(S[^02468S]*){35}'
matches = [match.group() for match in finditer(pattern, data)]
answer = max(matches, key=len)
print(len(answer))
# 2S3S5S3S
# 2S3S3S5