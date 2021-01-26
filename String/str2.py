def num_(n):
    copy = n

    N =0

    while copy > 0:
        d = copy % 10
        if d == 0:
            d = 5
        N = N*10 + d

        copy = copy//10

    copy = N
    N = 0
    while copy > 0:
        d = copy % 10
        N = N*10 + d
        copy = copy //10


    return N

a = int(input("Enter the num: "))
print(num_(a))

