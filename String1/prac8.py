"""
st1 = "__--_-__-"
            |     
st2 = "__-"
       |  
Ans = 2

"""

str1 = input()
str2 = input()
l = len(str2)
count = 0
for i in range(len(str1)):
    if str2 == str1[i:l+i]:
        count += 1
print(count)



















