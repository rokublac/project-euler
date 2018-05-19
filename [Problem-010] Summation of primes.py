"""
Project Euler 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
from math import ceil

def isPrime(num):
    limit = int(ceil(num ** 0.5))
    
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True
    
def primes(upper_limit):
    yield 2
    current = 3
    
    while current < upper_limit:
        if isPrime(current):
            yield current
        current += 2
        

print(sum(primes(2000000)))
    
    
        
