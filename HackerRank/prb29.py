n = int(input())
s = input()

conum =0
coupper =0
colower =0
cospec =0

for i in range(len(s)):
    if s[i].isupper():
        coupper += 1
    elif s[i].islower():
        colower += 1
    elif s[i].isnumeric():
        conum += 1
    else:
        cospec += 1

count =0

if conum ==0:
    count +=1
if coupper == 0:
    count += 1
if colower == 0:
    count += 1
if cospec == 0:
    count += 1

print(max(count, 6-len(s)))
