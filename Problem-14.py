'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

SEQUENCE_CACHE = {}
LIMIT = 1000000

highestSeq_length = 0
highestSeq_value = 0


for number in range(LIMIT):
    # currentValue will be modified within the proceeding while loop. We still want number to be static in this loop.
    currentValue = number
    
    # Number 0 and 1 both have a sequence of 1.
    if (currentValue == 1) or (currentValue == 0):
      highestSeq_value = currentValue
      highestSeq_length = 1
      continue
    
    # Base sequence length starts at 1 (0 and 1 will give you a Collatz sequence length of 1)
    sequenceLength = 1
    
    # For this, we assume all Collatz sequences end on 1 
    while currentValue != 1:
        try:
            # Since sequenceLength always start as one, it will always be one above the cache length we're looking for. That's why we check it to the minus 1.
            sequenceLength += SEQUENCE_CACHE[currentValue] - 1
            # If this statement does now throw an error, we have successfully found a cache value.
            break
        except KeyError:
          # If it fails, it means that the current number we are iterating through does is not cached. Therefore we continue the calculation.
            pass

        if currentValue % 2 == 0:
            # Even numbers
            currentValue = currentValue / 2
        else:
            # Odd numbers
           currentValue = (3 * currentValue) + 1
        sequenceLength += 1
    
    # Cache the number and it's corresponding sequence length
    SEQUENCE_CACHE[number] = sequenceLength

    # Keep track of the largest sequence length as well as its corresponding value.
    if sequenceLength > highestSeq_length:
        highestSeq_value = number
        highestSeq_length = sequenceLength 
        
print("Between 0-{0}, the number {1} has the longest Collatz sequence with a length of {2}.".format(LIMIT, highestSeq_value, highestSeq_length))
