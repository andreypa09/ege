
data = 'CBAAAABABCBAAAABCABACCCAB'
pairs = ["AB", "CB"]
i = 0
cnt = 0
max_len = 0
while i < len(data)-1:
    pair = data[i] + data[i+1]
    if pair in pairs:
        cnt += 1
        i += 2
        max_len = max(max_len, cnt)
    else:
        cnt = 0
        i += 1
print(max_len)