data = '111AAAAAA333333AA1111'
data = data.translate(str.maketrans('13579', '*****'))
max_len = 0
current_len = 2
for i in range(len(data) - 2):
    current_len += 1
    if data[i] == data[i + 1] == data[i + 2] == "*":
        current_len = 2
    max_len = max(current_len, max_len)
print(max_len)
