"""
Find duplicate elements in an array

1 2 4 6 2 9 9 4

Ans: 
2 4 9
"""
L = list(map(int, input("Enter the elements:").split()))

#L = [1,2,4.....]

#d ={
#    1: 1 ,
#    2: 2 ,
#    4: 2 ,
#    6: 1 ,
#    9: 2,
#       
#} 

d = {} 
for i in L:#4
    if i in d:
        d[i] += 1 # d[i] = d[i] + 1
    else:
        d[i] = 1

for key in d:
    if d[key] != 1:
        print(key, end = " ")

print()

