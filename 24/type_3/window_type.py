from string import digits, ascii_uppercase
# data = "XX01345A1XX"
#
# alpha = digits + ascii_uppercase
#
# good = alpha[:12]
# bad = alpha[12:]
#
# even = good[::2]
# l = 0
# max_length = 0
# for r in range(len(data)):
#     if data[r] in bad:
#         l = r + 1
#     else:
#         if data[l] == "0":
#             l += 1
#         if data[r] in even:
#             max_length = max(max_length, r - l + 1)
# print(max_length)


# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.


# data = "LOCIZQT00795CCAEL"
# with open("22359.txt") as f:
#     data = f.readline()
# alpha = digits + ascii_uppercase
#
# good = alpha[:15]
# bad = alpha[15:]
#
# ev5 = good[::5]
# l = 0
#
# substrings = []
# for r in range(len(data)):
#     if data[r] in bad:
#         l = r + 1
#         continue
#     while data[l] == "0":
#         l += 1
#     if data[r] in ev5:
#         substring = data[l:r+1]
#         if substring:
#             substrings.append((substring, r))
# ans = max(substrings, key = lambda x: int(x[0], 15))
# print(ans)
