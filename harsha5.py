def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest


# Driven code
a = 45
b = 34
c = 16
print(maximum(a, b, c))
