T = int(input())

for i in range(T):
    count = 0
    p = int(input())
    num = 2048
    if p>=num:
        count += p//num
        p= p%num
    num = 1024
    if p>=num:

        count += p//num
        p = p%num
    num = 512
    if p>=num:
        count += p//num
        p= p%num

    num = 256
    if p>=num:

        count += p//num
        p = p%num

    num = 128
    if p>=num:
        count += p//num
        p= p%num
    num = 64
    if p>=num:

        count += p//num
        p = p%num

    num = 32
    if p>=num:
        count += p//num
        p= p%num

    num = 16
    if p>=num:

        count += p//num
        p = p%num

    num = 8
    if p>=num:
        count += p//num
        p= p%num

    num = 4
    if p>=num:

        count += p//num
        p = p%num

    num = 2

    if p>=num:
        count += p//num
        p= p%num
    num = 1
    if p>=num:

        count += p//num
        p = p%num

    print(count)







