# Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
# Onределите в этом файле последовательность идущих подряд символов,
# представляющих собой запись максимального нечётного 12-ричного числа.
# В ответе запишите индекс (номер) первого символа (первой значащей цифры),
# с которого начинается запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.

# from string import ascii_uppercase, digits
# with open("22356.txt") as f:
#     data = f.readline()
# alpha = digits + ascii_uppercase
#
# good = alpha[:12]
# bad = alpha[12:]
#
# ev5 = good[1::2]
# string = ""
# index = 0
# maxi = 0
# for i in range(len(data)):
#     if string == "" and data[i] == "0":
#         continue
#     if data[i] in good:
#         string += data[i]
#     else:
#         string = ""
#     if data[i] in ev5 and maxi < int(string, 12):
#         maxi = int(string, 12)
#         index = i - len(string) + 1
# print(index)

