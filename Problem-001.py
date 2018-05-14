
"""
PROJECT EULER - PROBLEM 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
# Version 1
result = 0 # Add numbers that meet the condition

for num in range(1,1000): # Condition to get the numbers from 1 to 1000 (not including 1000)
    if num % 3 == 0 or num % 5 == 0:
        result += num

print(result)

# ----------------- An alternative is to use sets (thanks to Jason Hill for making me aware of sets for this problem) ----------------- #

# Version 2
# Using sets oer lists is faster in this context. Not a huge issue for this problem, but doesn't hurt to speed things up.
multOf3 = set(range(3,1000,3))
multOf5 = set(range(5,1000,5))
resultSet = multOf3.union(multOf5)
result = sum(resultSet)

print(result)

