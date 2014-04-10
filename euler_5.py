import math
def is_prime(n):
	sqrt_n = int(math.sqrt(n))
	if sqrt_n % 2 == 0:
		sqrt_n = sqrt_n + 1

	while sqrt_n >= 2:
		if n % sqrt_n == 0:
#			print "prime test: %d failed by %d" % (n, sqrt_n)
			return False
		sqrt_n = sqrt_n - 1
	return True


def primes_under(n):
	primes = []
	for num in range(2, n+1):
		if is_prime(num):
			primes.append(num)
	return primes

def max_number(n):
	nums = range(2, n+1)
	primes = primes_under(n)
	product = 1
	max = 0

	for prime in primes:
		max = 0
		for num in nums:
			exp = int(math.log(num, prime))
			if pow(prime, exp) == num:
				if exp > max:
					max = exp
					print "(prime, exp) = (%d, %d)" % (prime, exp)
		product = product * pow(prime, max)			
	return product




print max_number(20)	


