while True:

    n = int(input()) #4
    if n == 0:
        break
    l =list(map(int, input().split())) # 1, 4, 3, 2
    l1 = [0 for i in range(len(l))] # 1,4,3,2

    for j in range(len(l)):#3

        l1[ l[j]- 1 ] = j+1 # 
    

    if l1 == l:
        print("ambiguous")
    else:
        print("not ambiguous")

    

        





























