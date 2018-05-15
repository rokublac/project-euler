
'''
Project Euler - Problem 67 (Maximum path sum II)
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, find the maximum sum in the given triangle.
I am taking the bottom-up approach where I will find the maximum of each row in the pyramid and then sum it to the above adjacent number.
This will eventually eat the triangle (from the bottom up) and then end up with the largest sum at the peak. 

This will be down with recursion and it ends once the base case it hit. So it computes pretty quickly.

* Thanks to Jason Hill's blog for optimization
'''
 
# Read in pyramid from a text file
data = []
file = open('Problem-067.txt')
# Split each line into its own list
for line in file:
	data.append([int(i) for i in line.split(" ")])


def highestSumPath(pyramid, pyramidRow):
	for i in range(len(pyramid[pyramidRow])):
		# Adjacent postions - First comparison is one row down to the left, the second is one row down to the right.
		pyramid[pyramidRow][i] += max(pyramid[pyramidRow + 1][i], pyramid[pyramidRow + 1][i + 1])
	# Base case - once the algorithm has eaten enough of the pyramid that it only has one number left, return that, and that will be our answer.
	if len(pyramid[pyramidRow]) == 1:
		return pyramid[pyramidRow][0]
	else:
		# Keep eating from the bottom up
		return highestSumPath(pyramid, pyramidRow - 1)

# Starting from the second last row, since we are initially comparing the second last row to the last row
result = highestSumPath(data, len(data) - 2)

print(result)

