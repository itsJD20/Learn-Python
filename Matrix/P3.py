M = [[1, 2 ,3], #0
     [4, 5, 6], #1   
     [7, 8, 9]] #2

A = [[1, 4 ,7], #0
     [2, 5, 8], #1   
     [3, 6, 9]] #2


def print_mat(X):

    for i in range(len(X)):#0
        for j in range(len(X[i])):#3
            print(X[i][j], end = " ")#0,0
        print()


def trans(X):

    for i in range(len(X)):#2
        for j in range(i):#2 - 1
            X[i][j], X[j][i] = X[j][i], X[i][j] # 8, 6= 6,8

        

    return X

M = trans(M)
print_mat(M)


