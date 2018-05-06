# -*- coding: utf-8 -*-
"""
***SOLVED***

PROJECT EULER - PROBLEM 6
https://projecteuler.net/problem=6

"""
import time
import logging
from math import sqrt

logging.basicConfig(level=logging.DEBUG)

start_time = time.time()

numList = []
numList2 = []
baseNumSq = 0

for baseNum in range(1,101):
    
    baseNumSq = baseNum ** 2
    numList.append(baseNumSq)
    baseNum += 1

sumOfSquares = sum(numList)

for baseNum2 in range(1,101):
    numList2.append(baseNum2)

sumOfNumSquared = sum(numList2)
squareOfSumNumSq = sumOfNumSquared ** 2

result = squareOfSumNumSq - sumOfSquares
    
print('Sum of squares from 1 to 100 |', sumOfSquares)
print('Square of Sum of 1 to 100 |', squareOfSumNumSq)
print('Difference of Sum of squares and Square of Sum of 1 to 100 |', result)

print('--- %s seconds ---' %(time.time() - start_time))

    

