n = int(input())

for i in range(n):
    x,y,z = map(int,input().split())

    a = abs(x-z)#2

    b = abs(y-z)#1

    if a<b:
        print("Cat A")
    elif b<a:
        print("Cat B")
    else:
        print("Mouse C")