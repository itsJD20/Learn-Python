a = int(input("Enter the number: "))


for i in range(a):
    for j in range(i+1):

        if(i%2==0):
            print(1,end=" ")
        else:
            print(0,end=" ")

    print("")
  