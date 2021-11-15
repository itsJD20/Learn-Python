t = input()

h = int(t[0:2])

f = t[8:10]

if f == "PM" and h != 12:
    h += 12
if f == "AM" and h ==12:
    h = 0

print(str(h).zfill(2)+t[2:8])






