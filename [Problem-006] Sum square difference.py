# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
from math import sqrt

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



    

