# from string import digits, ascii_uppercase
# data = "XX01345A1XX"
#
# alpha = digits + ascii_uppercase
#
# good = alpha[:12]
# bad = alpha[12:]
#
# even = good[::2]
# max_len = 0
# for i in bad:
#     data = data.replace(i, ' ')
# for part in data.split():
#     while part and part[0] == "0":
#         part = part[1:]
#     while part and part[-1] not in even:
#         part = part[:-1]
#     max_len = max(max_len, len(part))
# print(max_len)