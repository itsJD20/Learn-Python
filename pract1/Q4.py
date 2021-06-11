"""
Accept 2 lists and print True if they have exactly same elements 
False if they have uncommon elements

1 5 7 9
9 5 7 1 1

Ans: True

13 15 7 9 9
9 5 7 13 1 15

Ans: False
"""


n = int(input("Enter the number: ")) 
L1 = list(map(int, input("First List: ").split()))
L2 = list(map(int, input("Second List: ").split()))

L1 = set(L1)
L2 = set(L2)

if L1 == L2:
    print("True")
else:
    print("False")
