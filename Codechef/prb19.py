T = int(input())

for i in range(1,T+1):

    A,B,C = map(int, input().split())

    if(A+B+C == 180):
        print("YES")

    else:
        print("NO")