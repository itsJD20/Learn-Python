T = int(input())

for i in range(T):
    s = input()#abba
    d= {
        "a": 0,
        "b": 0
    }

    for c in s:
        d[c] += 1

    print(min(d["a"],d["b"]))
