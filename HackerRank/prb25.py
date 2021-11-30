n = int(input())
s = input()

count = 0

level = 0

for i in range(len(s)):
    plevel = level

    if s[i] == "D":
    
        level -= 1
    else:
        level += 1
    if plevel == 0 and level == -1:
        count += 1
print(count)

        