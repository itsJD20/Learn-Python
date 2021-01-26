def revnum_(n):
    

    N = 0
    while n > 0:
        n1 = n%10
        N = N * 10 + n1
        n = n // 10

    return N

a = int(input(" Enter the num: "))

if(a == revnum_(a)):
    print("Palindrome")

else:
    print("Not Palindrome")



