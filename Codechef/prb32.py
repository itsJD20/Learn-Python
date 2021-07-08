T = int(input())

for i in range(T):
    s = int(input())

    if s < 1500:
        print("{:.2f}".format(2*s))

    else:
        print("{:.2f}".format(s +500 + (s*98/100)))
