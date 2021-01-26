M1 = [[1, 2 ,3], #0
      [4, 5, 6], #1   
      [7, 8, 9], #2
      [10, 11, 12]] #3

M2 = [[1, 5, 9], #0
      [2, 6, 10], #1   
      [3, 7, 11], #2
      [4, 8, 12]] #3


def print_mat(X):

    for i in range(len(X)):
        for j in range(len(X[i])):
                print(X[i][j], end = " ")

        print()

def addnum_mat(X, Y):

    for i in range(len(X)):#4 - 0
        for j in range(len(X[i])):#3 - 0
            X[i][j] += Y[i][j] 

    return X


M = addnum_mat(M1, M2)
print_mat(M)