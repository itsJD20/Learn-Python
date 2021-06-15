T = int(input())
ships = {
    "b": "BattleShip",
    "c": "Cruiser",
    "d": "Destroyer",
    "f": "Frigate",
}
for i in range(T):

    c = input()

    print(ships[c.lower()])



