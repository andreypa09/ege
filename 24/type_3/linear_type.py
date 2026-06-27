# Текстовый файл состоит из десятичных цифр и
# заглавных букв латинского алфавита.
# Onределите в этом файле последовательность
# идущих подряд символов, представляющих собой
# запись максимального кратного пяти 15-ричного числа.
# В ответе запишите индекс (номер) последнего символа
# (последней значащей цифры), которой заканчивается
# запись этого числа в прилагаемом файле.
# Нумерация символов в текстовом файле начинается с нуля.

from string import ascii_uppercase, digits
#
# # data = "LOCIZQT00795CCAEL"
with open("22359.txt") as f:
    data = f.readline()
alpha = digits + ascii_uppercase

good = alpha[:15]
bad = alpha[15:]

ev5 = good[::5]
string = ""
index = 0
maxi = 0
for i in range(len(data)):
    if string == "" and data[i] == "0":
        continue
    if data[i] in good:
        string += data[i]
    else:
        string = ""
    if data[i] in ev5 and maxi < int(string, 15):
        maxi = int(string, 15)
        index = i
print(index)

