# Still takes too long (~9 seconds)... hopefully I'll optimize soon.

from math import sqrt


def noOfFactors(num):
	noOfFactors = 0
	for i in range(1, int(sqrt(num)) + 1):
		if num % i == 0:
			noOfFactors += 1
	return noOfFactors * 2

# Initalize 0 variables
i = 0
triSeqNumber = 0
factors = 0
highestNoOfFactor = 0
highestNum = 0

while highestNoOfFactor <= 500:
	i += 1
	triSeqNumber += i

	factors = noOfFactors(triSeqNumber)

	if factors > highestNoOfFactor:
		highestNoOfFactor = factors
		highestNum = triSeqNumber

print("First triangular number with over 500 divisors: " + str(highestNum))
print("Number of divisors: " + str(highestNoOfFactor))

# --- Doing it with lists --- #

# triangleSeq = []
# factors = 0
# highestNoOfFactor = 1
# highestNum = 0

# while highestNoOfFactor <= 200:
# 		# Triangle seq. formula: n(n+1)/2
# 		triangleSeq.append(int(i * (i+1)/2))
# 		factors = noOfFactors(triangleSeq[-1])

# 		if factors > highestNoOfFactor:
# 			highestNoOfFactor = factors
# 			highestNum = triangleSeq[-1]
		
# 		if len(triangleSeq) > 5:
# 			del triangleSeq[0]
# 		i += 1

# print(highestNoOfFactor)
# print(highestNum)
