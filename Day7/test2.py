a = int(input("Enter the number: "))

for i in range(1,a+1):

    if(i%3==0 and i%7==0):
        print(i,"FizzBuzz")
    elif(i%7==0):
        print(i,"Buzz")
    elif(i%3==0):
        print(i,"Fizz")
    else:
        print(i,"nothing")