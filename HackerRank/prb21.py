t = int(input())

for j in range(t):

    a= int(input())#12

    s= 0#3

    l =[]
    while a != 0:#1
        s = (a%10)
        l.append(s)
        a //= 10
    count =0
    for i in range(len(l)):
        if a%l[i] ==0:
            count += 1
    print(count)