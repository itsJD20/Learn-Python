"""
Write a Program to accept a list of Blood and their number of samples 
and find the bloods with minimum number of samples

Eg 1:
Input
-----
5
A 10
B 15
AB 10
O 6
A+ 6
Output
------
O
A+
-------------------------
l1 = [10, 11,7, 8, 7, 2, 111]

mini = l1[0]

for i in range(len(l1)):
    if  l1[i] < mini:
        mini = l1[i]

print(mini)

for i in range(l1):
    if l1[i] == mini:
        print(i)

"""

L = int(input("Enter the number: "))

blood = {}

for i in range(L):
    B,N = input().split()
    N = int(N)
    blood[B] = N

mini = 10**10
for i in blood:
    if blood[i] < mini:
        mini = blood[i]

for i in blood:
    if mini == blood[i]:
        print(i)









