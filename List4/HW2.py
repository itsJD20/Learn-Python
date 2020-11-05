#input an Integer lists from the user and find the cumulative sum of the list and then find sum of cubes of elements of the final list
#Ex: 1 2 3 4
#1244


def cube(x):
    return x**3


l = list(map(int, input("L =").split()))
l1 = []
s = 0
for i in range(len(l)):
    s = s+l[i]
    l1.append(cube(s))

print(sum(l1))




