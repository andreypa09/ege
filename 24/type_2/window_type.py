data = "ABCBABABCBABCABCCAB"
pairs = ["AB", 'CB']
left = right = 0
max_len = 0
while right < len(data)-1:
    pair = data[right] + data[right+1]
    if pair in pairs:
        length = (right - left) // 2 + 1
        max_len  = max(length, max_len)
        right += 2
    else:
        left = right
        right += 1
print(max_len)