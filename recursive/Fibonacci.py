def fibonacci(x):

    if x == 1:
        return 1
    if x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)
         

N = int(input())
print(fibonacci(N))