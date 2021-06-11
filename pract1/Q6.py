"""
1 3 5 2 1 3
1 2 3 4 5 1

Ans: 2nd

Given 2 Lists find which one has more number of unique elements
"""

l1 = list(map(int, input("Enter the numbers: ").split()))
l2 = list(map(int, input("Enter the numbers: ").split()))

l1 = set(l1)
l2 = set(l2)

if l1 > l2:
    print("1st")
else:
    print("2nd")


