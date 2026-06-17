# data = "SAFASFAFAFS"
# breaks = [0]
# evens = '02468'
# max_len = 0
# current = 0
# i = 0
# while i < len(data)-1:
#     if data[i] in evens and data[i+1].isalpha():
#         j = i + 1
#
#         while j < len(data) and data[j] == data[i+1]:
#             j+= 1
#         if data[j] in evens:
#             breaks.append((i, j))
#         i = j
#     else:
#         i += 1
# print(breaks)
# for left, right in breaks:
#     distance = right - left + 1
#     max_len = max(max_len, distance)
# print(max_len)