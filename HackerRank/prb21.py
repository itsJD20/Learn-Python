n = int(input())

for i in range(n):
    grade = int(input())

    calculation = (grade//5) +1
    if grade < 38:
        print(grade)
    elif (5*calculation) - grade < 3:
        print(calculation*5)
    else:
        print(grade)
    