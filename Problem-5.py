"""

PROJECT EULER - PROBLEM 5 - SMALLEST MULTIPLE
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def checker(num):
    # Don't have to do range(1,10) since those numbers are a mulitple of 2520.
    for i in range(11,21): 
        if num % i == 0:
            continue
        else:
            return False 
    return True 

# 2520 since it has to be a multiple so it's faster to initialize it at 2520.
x = 2520 

# while num does not go into every number from 11 to 20, add 2520 until checker is True.
while checker(x) == False: 
    x += 2520

print(x)







