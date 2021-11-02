M2 = [[2, 5, 9], #0
      [2, 6, 10],#1   
      [3, 7, 11]]#2


def matrix(arr):
    rd = 0
    ld = 0
    for i in range(len(arr)):
        rd += arr[i][- i - 1]
        ld += arr[i][i]

    differ = abs(ld-rd)

    return differ


print(matrix(M2))





