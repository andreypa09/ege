data = "CBCABCBCABCACBBCBABCBABBCACA"
pairs = ["AB", "CB"]

breaks = [0]

i = 0
while i < len(data) -1:
    pair = data[i] + data[i+1]
    if pair in pairs:
        i += 2
    else:
        breaks.append(i)
        i += 1

breaks.append(len(data)-1)
max_len = 0
for i in range(1, len(breaks)):
    distance = breaks[i] - breaks[i-1] - 1
    max_len = max(max_len, distance)
print(max_len // 2)

