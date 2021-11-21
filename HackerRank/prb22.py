a1,v1,a2,v2 = map(int, input().split())

jumps = ((a2 -a1)/(v1-v2))
if jumps> 0 and jumps.is_integer():
    print("YES")
else:
    print("NO")





