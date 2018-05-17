'''
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# Factorial through recursion. Alternatively, you can just you factorial method from python's math library.
def factorial(num):
    if num == 0: 
    	return 1
    else:
    	return (num * factorial(num - 1))


x = factorial(100)
sumOfDigits = 0

# Iterate through the digits of the result and plus on each digit to sumOfDigits
for digit in str(x):
	sumOfDigits += int(digit)

print(sumOfDigits)
