'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt


# Get all factors of a number
def factors(num):
    results = set()
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            results.add(i)
            y = int(num/i)
            if y != num:
            	results.add(int(num/i))
    return results


# See if number is amicable or not
def isAmicable(num1):
	sum1 = 0
	sum2 = 0
	num2 = 0
	
	sum1 = sum(factors(num1))
	# Transfer value from sum1 to num2 for condition check
	num2 = sum1
	sum2 = sum(factors(sum1))

	if (sum1 == num2) and (sum2 == num1) and (sum1 != sum2):
		return(num1, num2)
	else:
		return False


amicalList = []
# Start at 220 since we know that's the lowest amical number.
counter = 220
# Find sum of all amicable numbers under 10,000
limit = 10000

while counter < limit:
	# Since we are getting pairs, check if other pair value in already received.
	if counter in amicalList:
		continue
	elif isAmicable(counter) != False:
		amicalList.append(isAmicable(counter)[0])
		amicalList.append(isAmicable(counter)[1])
		# Set counter to be the end pair value since no number will be amical below that value.
		counter = isAmicable(counter)[1]
	counter += 1

print(amicalList)

	
