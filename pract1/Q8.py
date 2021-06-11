"""
1 3 5 2 1 3 9                     # 1         
1 2 3 4 5 1 15                    # 2      

Ans: 2nd

find the list with maximum number of unique elements in comparison to both the lists.
"""

l1 = list(map(int, input("Enter the numbers: ").split()))
l2 = list(map(int, input("Enter the numbers: ").split()))

l1 = set(l1)#1 3 5 2 9
l2 = set(l2)#1 2 3 4 5 15

#count
count1 = 0 #1
count2 = 0 #1
for i in l1:#1
    if i not in l2:#1
        count1 += 1 #count = 1 1 1
for i in l2:
    if i not in l1:
        count2 +=1

if count1 > count2:
    print("1st")
else:
    print("2nd")







