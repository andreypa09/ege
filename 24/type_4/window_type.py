data = "abbacadbada"

left = 0
used = set()
string = ""
max_len = 0
for right in range(len(data)):
    ch = data[right]
    if ch in last_pos and last_pos[ch] >= left:
        used.remove(data[left])
        left += 1
    last_pos[ch] = right
    current_len = right - left + 1


    if current_len > max_len:
        max_len = current_len
        string = data[left:right + 1]
print(string, max_len)