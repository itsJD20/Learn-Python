"""
x = 1
y = 2
m = 2
2 8

- - - - _ - - - - -
1 2 3 4 5 6 7 8 9 10


100

m = 4 x = 7 y = 8
12 52 56 8

56

1 ... 68    1 ... 100  1 ... 100  1 ... 64
0
"""

T = int(input())#1
for i in range(T):
    M,x,y= map(int, input().split())#4 7 8
    L = list(map(int, input().split()))#12 52 56 8
    house = [0] * 100 #[0 0 0 0 0 0 0 0.......]
    house_per_cop = x*y #7*8= 56
    for house_num in L: #12
        for j in range(max(1,house_num - house_per_cop),min(100,house_num + house_per_cop)+1):
            house[j-1] = 1 #[1..........1]

    count = 0
    for k in house:
        if k == 0:
            count +=1

    print(count)

    














