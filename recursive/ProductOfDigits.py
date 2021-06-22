def POD(a):
    if 10>a>=0:
        return a 
    x = POD(a//10) * (a%10)
    return x

N = int(input("Enter the number: "))
print(POD(N))