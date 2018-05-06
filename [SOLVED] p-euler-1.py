# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:03:09 2017

@author: Benz

**SOLVED**

PROJECT EULER - PROBLEM 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
import logging

logging.basicConfig(level=logging.DEBUG)

numList = [] # Create list to store the multiples of 3 and 5

for num in range(1,1000): # Condition to get the numbers from 1 to 1000 (not including 1000)
    if num % 3 == 0 or num % 5 == 0:
        numList.append(num)

sumList = sum(numList) # sum the list of numbers to get the answer

logging.debug(sumList)