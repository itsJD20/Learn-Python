"""
n = 3
    1
  3 2 3
6 5 4 5 6
"""
n = int(input("Enter the number:"))

c = 1
i = 0
while i < n:
	j = 0
	while j < (n - 1 - i):
		print(" ", end =" ")
		j += 1

	
	j = 0
	while j < i+1:
		print(c+i-j, end = " ")

		j += 1

	
	
	j = 1
	while j < i+1:
		print(c+j, end = " ")

		j += 1
	
	

	
	print(" ")
	c += j
	i += 1
		








	

