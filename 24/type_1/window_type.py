data = "111AAAAA333"
data = data.translate(str.maketrans('13579', '*****'))
left = 0
max_len = 1
for right in range(len(data)):
    if data[right] == data[right-1] == data[right-2] == '*' and right >= 2:
        print(right, left)
        left = right - 1
    max_len = max(max_len, right - left + 1)
print(max_len)