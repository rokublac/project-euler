
"""
PROJECT EULER - PROBLEM 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# This code is not very efficient process, hopefully I'll get back to it.
def isPrime(num):
	"""Checks num for primality. Returns bool."""

	if num == 2:
		return True
	elif num < 2 or num % 2 == 0:	# even numbers > 2 not prime
		return False

		# factor can be no larger than the square root of num
	for i in range(3, int(num ** .5 + 1), 2):
		if not num % i: return False
	return True



def generatePrimes(n):
	"""Returns a list of prime numbers with length n"""
	
	primes = [2,]
	noOfPrimes = 1	# cache length of primes for speed
	testNum = 3 # number to test for primality

	while noOfPrimes < n:
		if isPrime(testNum):
			primes.append(testNum)
			noOfPrimes += 1
		testNum += 2

	return primes

print(generatePrimes(10001)[-1])

        
