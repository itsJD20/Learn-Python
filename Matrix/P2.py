M = [[1, 2 ,3], #0
     [4, 5, 6], #1   
     [7, 8, 9], #2
     [10, 11, 12]] #3

def print_mat(X):

    for i in range(len(X)):#0
        for j in range(len(X[i])):#3
            print(X[i][j], end = " ")#0,0
        print()

def addnum_mat(X, num):

    for i in range(len(X)):#2
        for j in range(len(X[i])):#3
            X[i][j] *= num

    return X 

M = addnum_mat(M, 15)
print_mat(M)