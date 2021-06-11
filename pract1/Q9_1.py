"""
Given a list find all pairs of numbers in the list:

Ex1:
L = [1,2,3,4]
Ans:
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

Ex2:
L = [1,1,1,1]
Ans:
1 1

Ex2:
L = [1,2,1,3]
Ans:
1 1
1 2
1 3
2 1
2 2 
2 3
3 1
3 2
3 3 

"""

l = list(map(int, input("enter the numbers: ").split())) #1 2 1 3
u = set()
for i in range(len(l)):#0
    for j in range(len(l)): #1
        if (l[i], l[j]) not in u:
            print(l[i], l[j]) #1 1, 1 2, 1,3 
            u.add((l[i], l[j])) #(1,1), (1,2), (1,3)

            
       


