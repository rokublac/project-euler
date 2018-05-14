'''
PROJECT EULER 4 - LARGEST PALINDROME PRODUCT

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

num1 = 900 # highest palindrome will be within the multiples of some number from 900-99
largestPal = 0 # Set variable to be zero first. Will store largest palindrome

while num1 < 1000: # Three digit floor condition for num1
    for num2 in range(999,-1,-1):# number ceiling for num2, counter reverse by one interval
        pNum = num1 * num2
        numStr = str(pNum) # convert int to string for slice
        if numStr == numStr[::-1]: # read number string backwards to check for palindrome
          if pNum > largestPal:
              x, y = 0, 0   
              x, y = num1, num2 # print multiplying numbers
              largestPal = pNum
          
    num1 += 1

print("The largest palindrome made from a product of two 3-digit numbers is {0} times {1} = {2}.".format(x, y, largestPal))

