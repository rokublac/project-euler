'''
Project Euler - Problem 16 (Power Sums)

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

x = 2**1000
sumOfDigits = 0

# Iterate of the string of x
for eachNumber in str(x):
    # Convert string to int before adding it to the sum
    sumOfDigits += int(eachNumber)

print(sumOfDigits)
