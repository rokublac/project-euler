# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fibSeq = [1,1]
numOfDigits = 0

while True:
	fib = fibSeq[-1] + fibSeq[-2]
	fibSeq.append(fib)
	numOfDigits = len(str(fib))

	# Break from loop once a number with a thousand digits in obtained
	if numOfDigits == 1000:
		break

print(len(fibSeq))



