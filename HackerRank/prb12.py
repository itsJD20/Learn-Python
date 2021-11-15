n = int(input())
arr = list(map(int, input().split()))

d={}
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1

    else:
        d[arr[i]] = 1
"""
"5": 2
"4": 2
"6": 2
"3": 2
"""

h = -1#2
k = 0#3
for i in d:
    if (i<k and d[i]==h) or d[i]>h: 
        
        h = d[i]
        k = i


print(k)


