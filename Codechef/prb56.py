S = input()

n = int(input())
a = set()
for i in S:
    a.add(i)
    
for i in range(n):

    w = input()
    match = True
    for j in w:
        if j not in a:
            match = False
            break

    if match:
        print("Yes")
    else:
        print("No")

