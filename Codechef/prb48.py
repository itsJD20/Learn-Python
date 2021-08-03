"""
3 6
CLICK 1
CLICK 2
CLICK 3
CLICK 2
CLOSEALL
CLICK 1



____1  open1 
____2  close0
____3  close



1
2
3
2
0
1
"""

n,k = map(int,input().split()) #3,6

post_status = [0] * n #[0,0,0]
num_open = 0 #1
for i in range(k):#6
    s = input().split() #["CLICK", "1"]
    if s[0] == "CLOSEALL":
        num_open = 0
        post_status = [0]*n

    else:
        post_index = int(s[1]) - 1 # 0
        if post_status[post_index] == 0:
            num_open += 1
            post_status[post_index] = 1

        else:
            num_open -= 1
            post_status[post_index] = 0
    print(num_open)





















