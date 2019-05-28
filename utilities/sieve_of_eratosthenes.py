# Prime number genetor with sieve of Eratosthenes.
# This algorithm will generate a list of prime up until given limit. Handy function for algorithm challenges.
# Computational time exponetially increases. Starts to grind once limit >= 100 000. Have a look at 'Sieve of Atkins' for an efficient high limit prime generating algorithm.

from math import sqrt

def sieveOfEratosthenes(limit):
  # initially all numbers is looked at as a prime. Will remove non primes later.
  # start list with first prime - 2
  primesList = [2]
  for i in range(3,limit+1):
      primesList.append(i)

  i = 2

  while(i <= int(sqrt(limit))):
    # if i is in the list, delete all mutiple of it.
      if i in primesList:
          # j will give mutiples of i since its starting on i*i and increments up in i
          for j in range(i*2, limit+1, i):
              if j in primesList:
                  # deleting the multiple if found in list
                  primesList.remove(j)
      i += 1

  return primesList
