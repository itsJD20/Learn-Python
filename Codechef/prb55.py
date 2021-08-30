T = int(input())

for i in range(T):
    n,k = map(int, input().split())

    a = list(map(int, input().split()))
    ans = 0 #

    for j in range(n): #
        if a[j] <= k:
            k = k-a[j]
            ans = ans *10+1
        else:
            ans = ans * 10 + 0

    print(ans)





    



   