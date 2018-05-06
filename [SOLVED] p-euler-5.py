"""
*** SOLVED ***

PROJECT EULER - PROBLEM 5 - SMALLEST MULTIPLE
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
import logging
import time

logging.basicConfig(level=logging.DEBUG)

start_time = time.time()

def checker(num):
    for i in range(11,21): #Don't have to do 1 to 10 since we already know its a mulitple of 2520.
        if num % i == 0:
            continue
        else:
            return False # Return false if condition is not met
    return True # Return true if num goes into everything

x = 2520 # 2520 since it has to be a multiple so no point going up by one.
while checker(x) == False: # while num does not go into every number from 11 to 20, add 2520 until checker is True.
    x += 2520

    
    
logging.debug(x)
logging.debug('--- %s seconds ---' %(time.time() - start_time))






