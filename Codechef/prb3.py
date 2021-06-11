T = int(input())
a= []
for i in range(T):
    A,B = map(int,input().split())
    a.append([A, B]) # a[[1, 2],[3, 4]]

for i in range(T):
    print(a[i][0]+ a[i][1])