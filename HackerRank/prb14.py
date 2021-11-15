n,k = map(int, input().split())
bill = list(map(int, input().split()))
charged = int(input())

total = sum(bill)
actual = (total - bill[k]) // 2

owe = charged - actual

if charged == actual:
    print("Bon Appetit")
else:
    print(owe)
