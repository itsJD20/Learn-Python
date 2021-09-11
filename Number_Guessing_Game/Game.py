import random

def rand(l,u):

    return int(l + random.random() * (u-l))


a = 1
b = 1000

r = rand(a,b)
f =input("Enter the name of 1st Player: ")
s =input("Enter the name of 2nd Player: ")

attempts = 10
p_num = 1
while True:
    if attempts == 0:
        print("Lmao! You Lose")
    if p_num == 1:
        player = f
        p_num = 2
    else:
        player = s
        p_num = 1
    user = int(input(player + ": "))
    if user == r:
        print(player + " WIN ")
        break
    elif user > r:
        print("GIVE A SMALLER NUMBER")
    else:
        print("GIVE A BIGGER NUMBER")

    attempts -= 1





    




