from string import digits, ascii_uppercase, printable
# alph = digits + ascii_uppercase
# print(alph)
data = "XZ1234AZZ"
alph = digits + ascii_uppercase

good = alph[:16]
bad = alph[16:]
for i in bad:
    data = data.replace(i, ' ')
print(data.split())