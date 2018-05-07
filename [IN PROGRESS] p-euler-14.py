'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

## needs fixing, taking too long.

xlist = []
longestLengthVal = 0
longestLength = 0
temp = 0

for x in range(2,100):
  xlist.append(x)
  temp = x
  while xlist[-1] != 1:
    if(x % 2 == 0):
      x = x/2
    else:
      x = (3 * x) + 1
    xlist.append(int(x))
    
  if len(xlist) > longestLength:
    longestLengthVal = temp
    longestLength = len(xlist)
    print(longestLengthVal, longestLength)
    
  del xlist[:]
