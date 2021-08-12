"""
L1 = ["ala", "bu", "kala", "du", "mala", "chu"]
ch = "chu"
Ans = True

L2 = ["ala", "bu", "kala", "du", "mala", "chu"]
ch = "xucu"
Ans = False

Find if the word ch is present in the list
"""

L1 = input().split() #ala, bu, kala
ch = input()#kala
a = False

for i in range(len(L1)): # ala
    if ch == L1[i]:
        a = True
        break
 
if a:
    print(True)
else:
    print(False)

        