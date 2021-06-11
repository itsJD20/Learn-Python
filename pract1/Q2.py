"""
Given 2 lists find the common elements
Ex:
1 3 9 7 5 2 7 #6
9 8 7 6 3

Ans:
3 7 9
"""

L1 = list(map(int, input("Enter the numbers: ").split()))
L2 = list(map(int, input("Enter the numbers: ").split()))
L = []


for i in range(len(L1)): #3
    for j in range(len(L2)): #9
        if(L1[i]==L2[j]):
            L.append(L1[i])
            
newL = list(set(L))
for i in newL:
    print(i, end = " ")

print(" ")

# LX = list(newL)        
            







