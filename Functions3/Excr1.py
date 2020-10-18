a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))

def call_smallest(num1, num2):
    if(num1<num2):
        return num1, num2
    else:
        return num2, num1
    
        
def GCD(a, b):
    a, b = call_smallest(a, b) 
    HCF = 1
    for i in range(1, a+1):
        if(a%i==0 and b%i==0):
            HCF = i
    return HCF

print(GCD(a, b))
