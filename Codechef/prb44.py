def digit(a):
    count = 0

    while a != 0:
        count +=1
        a //= 10
    return count

N = int(input())

if digit(N) == 1:
    print(1)
elif digit(N) == 2:
    print(2)
elif digit(N) == 3:
    print(3)
else:
    print("More than 3 digits")


