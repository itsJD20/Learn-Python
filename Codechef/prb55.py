T = int(input())

for i in range(T):
    n,k = map(int, input().split())

    a = list(map(int, input().split()))
    ans = 0 #

    for j in range(n): # 10 8 
        if a[j] <= k:
            k = k-a[j]
            ans = ans *10+1
        else:
            ans = ans * 10 + 0
    new_ans = str(ans) #10

    print("0"*(n-len(new_ans))+ new_ans)





    



   