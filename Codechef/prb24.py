def palindrome(a):

    s = 0
    l = 0


    while a != 0:


        s = a%10
        l = (l*10) +s
        a//= 10

    return l

T = int(input())

for i in range(T):

    N = int(input())


    if(palindrome(N) == N):
        print("wins")

    else:
        print("loses")