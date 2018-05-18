'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from math import sqrt


# Get all factors besides itself
def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            y = int(n/i)
   			# Get all factors besides itself
            if y != n:
            	results.add(int(n/i))
    return results


# Perfect, Deficient, Abundant 
def PDA(num):
	# 1 is not a perfect number since itself is it's only divisor. We only sum factors that are not iteself.
	if num == 0:
		return("Zero is zero. It's special")
	elif num == 1:
		return('deficient')
	elif sum(factors(num)) == num:
		return('perfect')
	elif sum(factors(num)) > num:
		return('abundant')
	else:
		return('deficient')

# Use dictionaries for faster lookup.
# Create a dictionary of numbers
dictNumbers = {}
for i in range(1,28124):
	dictNumbers[i] = i

# Create a dictionary of abundant numbers
abundants = {}
for i in dictNumbers:
	if PDA(i) == 'abundant':
		abundants[i] = i

# Iterate over the abundant numbers and remove numbers from the dictionary that is a sum on two abundant numbers
for i in abundants:
	for j in abundants:
		total = i + j
		if total in dictNumbers:
			dictNumbers.pop(total)

print(sum(dictNumbers))
