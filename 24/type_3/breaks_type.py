# from string import digits, ascii_uppercase
#
# data = "XX01345A1XX"
# breaks = [0]
# alpha = digits + ascii_uppercase
# bad = alpha[12:]
# good = alpha[:12]
# even = good[::2]
# for i in range(len(data)):
#     if data[i] in bad:
#         breaks.append(i)
#
# breaks.append(len(data))
#
# max_len = 0
# for i in range(1, len(breaks)):
#     part = data[breaks[i-1] + 1:breaks[i]]
#     while part and part[0] == "0":
#         part = part[1:]
#     while part and part[-1] not in even:
#         part = part[:-1]
#     max_len = max(max_len, len(part))
# print(max_len)

from string import digits, ascii_uppercase

data = "LOCIZQT00795CCAEL"
breaks = [0]
alpha = digits + ascii_uppercase
bad = alpha[15:]
good = alpha[:15]
even = good[::5]
for i in range(len(data)):
    if data[i] in bad:
        breaks.append(i)

breaks.append(len(data))
candidates = []
for i in range(1, len(breaks)):
    left = breaks[i-1] + 1
    right = breaks[i]
    part = data[left:right]

    while part and part[0] == "0":
        part = part[1:]

    for j in range(len(part)-1, -1, -1):
        if part[j] in even:
            number = part[:j+1]
            end_index = right - (len(part) - j)
            candidates.append((number, end_index))
ans = max(candidates, key=lambda x: int(x[0], 15))
print(ans)