import math
def isPrime(n):
	sqrt_n = int(math.sqrt(n))
	if sqrt_n % 2 == 0:
		sqrt_n = sqrt_n + 1

	while sqrt_n >= 2:
		if n % sqrt_n == 0:
#			print "prime test: %d failed by %d" % (n, sqrt_n)
			return False
		sqrt_n = sqrt_n - 1
	return True

def primesUnder(n):
	primes = []
	count = 0
	currentNumber = 2
	while n > count:
		if isPrime(currentNumber):
			primes.append(currentNumber)
			count = count + 1
		currentNumber = currentNumber + 1
	return primes

print primesUnder(10001).pop()
