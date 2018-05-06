'''
Project Euler - Problem 3 (Long way - using mulitlpe fuctions and lists)
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


import logging
import math 
import time

start_time = time.time()
logging.basicConfig(level=logging.DEBUG)

### Function 1 - Get list of factors for a number
def getFactors(number):
    factorsList = []
    originalNumber = number
    for potentialFactor in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            factorsList.append(potentialFactor)
            factorsList.append(number // potentialFactor)
    return [originalNumber, factorsList] 

# Function 1 debug
# logging.debug(getFactors(600851475143))

### Function 2 - Check if number is a prime
def checkIfPrime(number):
    return len(getFactors(number)[1]) == 2

# Function 2 debug
# logging.debug(checkIfPrime(600851475143))

###
allFactors = getFactors(600851475143)[1] # Create a list of all factors for the input number
largestPrime = 0 # Initially zero but will store the largest prime 

for factor in allFactors: # Iterate through the list of factors
    if checkIfPrime(factor) and factor > largestPrime: # Check if the number is a prime and store if larger than previous prime number.
        largestPrime = factor # Stores the largest prime. Onc

print('Largest prime factor of %s is %s' % (getFactors(600851475143)[0], largestPrime))
print("--- %s seconds ---" % (time.time() - start_time))


