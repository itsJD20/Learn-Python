L = float(input("Listening: "))
R = float(input("Reading: "))
W = float(input("Writing: "))
S = float(input("Speaking: "))


avg = (L + R + W + S) / 4

print("Average of four components: ", avg)
print("Overall Score: ", round(avg))


