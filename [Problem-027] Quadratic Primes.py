# https://projecteuler.net/problem=27

from math import sqrt

#prime generator with sieve of Eratosthenes
def sieveOfEra(limit):
  primesList = [2]
  for i in range(3,limit+1):
      primesList.append(i)
  i = 2
  while(i <= int(sqrt(limit))):
      if i in primesList:
          for j in range(i*2, limit+1, i):
              if j in primesList:
                  primesList.remove(j)
      i += 1
  return primesList

# prime checker
def isPrime(num):
  if (num < 2):
    return False
  else:
    for i in range(2, int(sqrt(num)+1)):
      if (num % i == 0):
        return False
    else:
      return True


# require two seperate lists to iterate over
primes1000 = sieveOfEra(1000)
primes = primes1000[:]

# initial largest n set to 0
largest = 0

#looping through a quadratic equation
for b in primes1000:
	for a in primes1000:
		n = 0
		#positive a and b
		while True:
			quadratic = n**2+a*n+b 
			if quadratic not in primes:
				if isPrime(quadratic):
					primes.append(quadratic)
				else:
					if n > largest:
						largest = n
						abProduct = a*b
					break
			n += 1

		n = 0
		#negative a and positive b
		while True:
			quadratic = n**2-a*n+b 
			if quadratic not in primes:
				if isPrime(quadratic) and quadratic > 0:
					primes.append(quadratic)
				else:
					if n > largest:
						largest = n
						abProduct = -1*a*b
					break
			n += 1

#printing the largest product
print(abProduct)
