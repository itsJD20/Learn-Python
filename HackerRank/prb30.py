s = input()

count = 0
for i in range(0,len(s), 3):
    if s[i] != "S":
        count += 1
    if s[i+1] != "O":
        count += 1
    if s[i+2] != "S":
        count += 1

print(count)
