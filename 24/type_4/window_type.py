# data = "abbacadbada"
#
# left = 0
# used = set()
# string = ""
# max_len = 0
# for right in range(len(data)):
#     ch = data[right]
#     if ch in last_pos and last_pos[ch] >= left:
#         used.remove(data[left])
#         left += 1
#     last_pos[ch] = right
#     current_len = right - left + 1
#
#
#     if current_len > max_len:
#         max_len = current_len
#         string = data[left:right + 1]
# print(string, max_len)




# data = "TTTTUUTTTWTTTTUTTTTWTUUTWTUVWXYZTUWXZYTTTTTTTUTTUTTTTTUTUXXXXXZZZTTTT"
#
# left = 0
# counter = 0
# k = 5
# max_len = 0
# for right in range(len(data)):
#     if data[right] == "T":
#         counter += 1
#
#     while counter > k:
#         if data[left] == "T":
#             counter -= 1
#         left += 1
#     if counter == k:
#         max_len = max(right - left + 1, max_len)
#
# print(max_len)



# data = "ABCDEEABDEECEDEB"
with open("2425.txt") as f:
    data = f.readline()
left = 0
counter = 0
k = 3
max_len = 0
for right in range(len(data)):
    if data[right] == "A":
        counter += 1

    while counter > k:
        if data[left] == "A":
            counter -= 1
        left += 1
    if counter <= k:
        max_len = max(right - left + 1, max_len)

print(max_len)