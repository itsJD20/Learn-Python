"""
st1 = "abcdef"
st2 = "edc"
Ans = True

st1 = "abcdef"
st2 = "bcd"
Ans = False

find if the reverse of the 2nd string is present in the 1st string
"""

def rev(s):
    return s[ :: -1] 

str1 = input()
str2 = input()
l = len(str2)
found = False
for i in range(len(str1)):
    if str1[i: l+i]== rev(str2):
        found = True
        break

print(found)






