import math

def get_primes(n):
	l = [2]
	for num in range(3,n):
#		print "num: %d" % (num)
		for prime in l:
#			print "prime: %d" % (prime)
			if (num % prime) == 0:
				break
			if l[len(l) - 1] == prime:
				l.append(num)
#				print l
				break
	return l

def get_primes2(n):
	primes = []
	nums = range(2, n)
	nums.reverse()
	remn_cnt = len(nums)
	while remn_cnt > 0:
		prime = nums.pop()
		primes.append(prime)
		nums = filter(lambda x: x % prime != 0, nums)
		remn_cnt = len(nums)
	return primes


def largest_prime(primes, n):
	largest = 0
#	print primes
	for prime in tuple(primes):
		if n % prime == 0:
			largest = prime
	return largest


def is_prime(n):
	sqrt_n = int(math.sqrt(n)) 
	if sqrt_n % 2 == 0:
		sqrt_n = sqrt_n + 1

	while sqrt_n <= 2:
		if n % sqrt_n == 0:
			print "is_prime: %d divided by %d" % (n, sqrt_n)
			return False

		sqrt_n = sqrt_n - 2
	return True


def largest_prime(n):
	num = int(n/2)+1
	while num != 2:
		if n % num == 0:
			print "%d divided by %d" % (n, num)
			if is_prime(num):
				return num
		num = num - 1



#n = 600851475143
n = 13195

#print largest_prime(get_primes(n), n)
#print get_primes2(n)
print "result: %d" % (largest_prime(n))


