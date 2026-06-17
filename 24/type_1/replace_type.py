# with open('files/13866.txt') as f:
#     data = f.readline()
data = '111AAAAAA333333AA1111'
data = data.translate(str.maketrans('13579', '*****'))
while "***" in data:
    data = data.replace("***", "** **")

print(data.split())
