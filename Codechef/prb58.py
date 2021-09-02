T = int(input())

for i in range(T):
    A, B = map(int, input().split()) #2, 0

    n = 1 #3

    while True:
        if n%2 == 1 and n <= A:
            A -= n 
        elif n%2 == 1 and n > A:
            print("Bob")
            break
        elif n%2 == 0 and n <= B:
            B -= n
        elif n%2 == 0 and n > B:
            print("Lamik")
            break

        n += 1

    

    


        
