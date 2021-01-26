weight = int(input("Weight: "))
unit = input('(L)bs or (K)g:')

if unit.upper() == "L":
    con_weight = weight * 0.45
    print("your weight is",con_weight,"kilos")
else:
    con_weight = weight // 0.45
    print("your weight is",con_weight,"pounds")
