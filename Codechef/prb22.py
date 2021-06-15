N = int(input())
A = list(map(int, input().split()))
evencount = 0
oddcount = 0
for w in A:

    if(w % 2 == 0):
        evencount += 1

    else:
        oddcount += 1

if evencount > oddcount:
    print("READY FOR BATTLE")

else:
    print("NOT READY")


