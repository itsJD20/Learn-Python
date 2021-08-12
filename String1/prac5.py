"""
st1 = "abcd"
st2 = "cd"
Ans = True

st1 = "abcd"
st2 = "ad"
Ans = False

find if the string is there in the other string

"""

str1 = input()
str2 = input()
l = len(str2)
found = False
for i in range(len(str1)):
    if str2 == str1[i:l+i]:
        found = True
        break 

if found:
    print(True)
else:
    print(False)

