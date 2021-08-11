"""
str1 = "ala bu"
str2 = "bu ala"
Ans = True

str1 = "ala bu"
str2 = "bu alai"
Ans = False

str1 = "alabu"
str2 = "bu ala"
Ans = False

Check if both the string has same characters
"""

str1 = input()
str2 = input()


d1 ={}
d2 ={}

for i in str1:
    if i in d1:
        d1[i] +=1
    else:
        d1[i] = 1


for j in str2:
    if j in d2:
        d2[j] +=1
    else:
        d2[j] = 1
 
"""
if d1 == d2:
    print("True")
else:
    print("False")


d1 = {
    "a": 1
}

d2 = {
    "a": 2
}
""" 

if len(d1) != len(d2):
    print(False)
else:
    eq = True
    for i in d1:
        if i not in d2 or d2[i] != d1[i]:
            eq = False
            break
    
    if eq:
        print(True)
    else:
        print(False)
    

















