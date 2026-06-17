data = "ABCBABABCBABCABCCAB"

pair = ["AB", "CB"]

for i in pair:
    data = data.replace(i, "*")

for i in "ABC":
    data = data.replace(i, " ")

max_len = len(max(data, key=len))
print(max_len, data)