"""
1 3 5 2 1 3                               # 1 3 5 2 = 11
1 2 3 4 5 1                               # 1 2 3 4 5 = 15

Ans: 2nd

find the list with maximum sum of unique elements
"""

l1 = list(map(int, input("Enter the numbers: ").split()))
l2 = list(map(int, input("Enter the numbers: ").split()))

l1 = sum(list(set(l1)))
l2 = sum(list(set(l2)))

if l1 > l2:
    print("1st")
else:
    print("2nd")

