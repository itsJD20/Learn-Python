# Matrix Vertical Flip
M = [[1, 2 ,3], #0
     [4, 5, 6], #1   
     [7, 8, 9], #2
     [10, 11, 12]] #3


A = [[7, 8 ,9], #0
     [4, 5, 6],    #1
     [7, 8, 9],    #2
     [10, 11, 12]]    #3
    


def print_mat(X):

    for i in range(len(X)):
        for j in range(len(X[i])):
            print(X[i][j], end =" ")
        print()


def flip(X):
    for i in range((len(X))//2):#0
        for j in range(len(X[i])):#0
            X[i][j] , X[len(X) - i - 1][j] = X[len(X) - i - 1][j], X[i][j]

    return X

print_mat(A)
print_mat(flip(A))


    
    