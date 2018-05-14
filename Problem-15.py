'''
Project Euler - Problem 15 (Lattice paths)
https://projecteuler.net/problem=15
'''
# We only can navigate in two direction - right and down. Right will equal 1 and down will equal 0.
# eg. right, right, down, down = 1100
# This then turns into a arrangement binary bits permutation problem. We can then use the binomial theorem equation to figure out the result.
# n choose n/2

from math import factorial


def latticePath(size):
	result = factorial(size * 2) / ((factorial(size)))**2
	print(int(result))

latticePath(20)

