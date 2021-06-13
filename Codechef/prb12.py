N = int(input()) #5
line = []
for i in range(N):
    S,T = map(int, input().split())
    line.append([S, T])
#[[1, 2], [4, 6], [9, 12], [16, 20], [25, 22]]
for i in range(1,N):# 5 - 4
    for j in range(2):# 0
        line[i][j] += line[i-1][j]

W = 1
L = 0 
for i in range(N):

    if(line[i][0] > line[i][1]):
        curL = line[i][0] - line[i][1]
        curW = 1

    else:
        curL = line[i][1] - line[i][0]
        curW = 2
    if curL > L:
        L = curL 
        W = curW

    
print(W, L)



    
