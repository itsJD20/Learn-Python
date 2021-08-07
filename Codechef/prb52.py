"""
AB??ED
AB?ED?

"""
T = int(input())
for i in range(T):
    X = input()
    Y = input()

    match = True


    for j in range(len(Y)):
        if X[j] == "?" or Y[j]=="?" or X[j] == Y[j]:
            continue
        else:
            match = False
            break

    if match:
        print("Yes")
    else:
        print("No")




