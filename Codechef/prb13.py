T = int(input())

for i in range(1,T+1):
    A,B,C = map(int, input().split())
   



    if (A>C>B) or (B>C>A) and (A != B != C):
        print(C)

    elif (A>B>C) or (C>B>A) and (A != B != C):
        print(B)

    elif (C>A>B) or (B>A>C) and (A != B != C):
        print(A)

