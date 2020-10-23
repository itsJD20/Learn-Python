n = int(input("Enter the number: "))

l = []
for i in range(1,n+1):
    l.append(int(input()))#2,3,4

def cube(num):
    return num**3


for i in range(n):
    l[i] = cube(l[i])

print(l)