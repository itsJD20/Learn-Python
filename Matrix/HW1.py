M1 = [[1, 2 ,3], #0
      [4, 5, 6], #1   
      [7, 8, 9]] #2

M2 = [[1, 5, 9], #0
      [2, 6, 10], #1   
      [3, 7, 11]] #2

# Print M1 + transpose(M2)

def print_mat(X):

    for i in range(len(X)):#0
        for j in range(len(X[i])):#3
            print(X[i][j], end = " ")#0,0
        print()

def trans(X):
    for i in range(len(X)):
        for j in range(i):
            X[i][j], X[j][i] = X[j][i], X[i][j]

    return X

def sum_cal(X, Y):
    for i in range(len(X)):#0
        for j in range(len(X[i])):
            X[i][j] += Y[i][j]

    return X

M = trans(M2)
M3 = sum_cal(M1, M)
print_mat(M3)

#print_mat(sum_cal(M1, trans(M2)))







