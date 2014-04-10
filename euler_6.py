def range_pow(n):
	total = 0
	for num in range(1, n+1):
		total = total + pow(num, 2)
	return total

def sum_pow(n):
	total = 0
	for num in range(1, n+1):
		total = total + num
	return pow(total, 2)

n = 100
print sum_pow(n) - range_pow(n)
