n,k = map(int,input().split())

h = list(map(int, input().split()))

h1 =h[0]
for i in range(len(h)):
    if h[i] > h1:
        h1 = h[i]
dose =0
if k <= h1:

    dose = abs(k - h1)

print(dose)



