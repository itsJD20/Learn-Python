T = int(input())

for i in range(T):

    B = int(input())

    if B < 4:
        print(0)
    else:
        B = (B-2)//2

        print(B * (B+1) // 2)