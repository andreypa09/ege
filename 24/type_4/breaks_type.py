data = "TTTTUUTTTWTTTTUTTTTWTUUTWTUVWXYZTUWXZYTTTTTTTUTTUTTTTTUTUXXXXXZZZTTTT"

breaks = [0]
k = 5
max_len = 0
for i in range(len(data)):
    if data[i] == "T":
        breaks.append(i)
breaks.append(len(data))

for i in range(1,len(breaks) - k):
    right = breaks[i + k]
    left = breaks[i-1]

    max_len = max(max_len, right - left -1)

print(max_len)


