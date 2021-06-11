"""
Write a Program to accept a list and a number from the user and 
find the number of pairs in the list that add up to the number.

Ex1:
L = [1,2,3,4,5,6,7,8]
n = 6

Ans: 2

Reason: 1 + 5 = 6, so 1 and 5 is a pair and 2 + 4 = 6, so 2 and 4 is a pair.
Since there are only 2 pairs that adds up to 6 so the ans is 2 

Ex2:
L = [5,5,5,5,5,5,5,5]
n = 10

Ans: 1

Reason: 5 + 5 = 10, so (5,5) is the only possible pair. Hence ans is 1.


"""
l = list(map(int, input("List: ").split()))
n = int(input("Enter the number: "))
count = 0
u = set()
for i in range(len(l)):#2
    for j in range(i+1, len(l)):
        if (l[i], l[j]) not in u or (l[j], l[i]) not in u:
            if ((l[i] + l[j]) == n):
                count += 1
                u.add((l[i], l[j]))
        
            

print(count)



