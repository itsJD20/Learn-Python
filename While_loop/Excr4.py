l = list(map(int, input("Input numbers:").split()))
s = 0
i = 0

while i < len(l):
    s = s + l[i]
    i += 1
print(s)