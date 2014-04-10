import math
def is_prime(n):
	sqrt_n = int(math.sqrt(n))
	if sqrt_n % 2 == 0:
		sqrt_n = sqrt_n + 1

	while sqrt_n >= 2:
		if n % sqrt_n == 0:
			print "prime test: %d failed by %d" % (n, sqrt_n)
			return False
		sqrt_n = sqrt_n - 1
	return True

def largest_prime(n):
	half_n = int(math.sqrt(n))
#	half_n = int(n/2) + 1
	if half_n % 2 == 0:
		half_n = half_n + 1

	while half_n > 2:
		if n % half_n == 0:
			print "%d divided by %d" % (n, half_n)
			if is_prime(half_n):
				return half_n
		half_n = half_n - 2

#n = 13195
n = 600851475143
print largest_prime(n)

