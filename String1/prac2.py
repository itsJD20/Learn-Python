"""
str1 = "ala bu"
Ans = "ub ala"

Reverse a string...
"""



s = input()

str1 = ""
for i in range(len(s)-1, -1, -1):
    str1 += s[i]

print(str1)