"""
1 1 1 2 1 4 1 3 3 3 2 1

ans: 1

Accept a list and find the element with maximum frequency
"""

L = list(map(int, input("Enter the elements:").split()))

d = {}

for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

new = -1
newI = 0
for i in d:
    if d[i] > new:
        new = d[i]
        newI = i

print(newI, ":", new)


