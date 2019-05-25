#  Finding cycles using a dictionary

def cycleFinder(denominator):
  table = {}
  remainder = 1
  index = 1

  while(True):
    if remainder in table:
      return ((index - table[remainder]), index)
      index += 1
    else:
      table[remainder] = 1
      remainder = (remainder * 10) % denominator
      index += 1


def longestCycle(limit):
  longest = 0
  denominator = 0

  for num in range(2, limit):
    if (cycleFinder(num)[0] > longest):
      longest = cycleFinder(num)[0]
      denominator = cycleFinder(num)[1]
  return longest, denominator, limit



print("The longest reciprical cycle from 1/2 to 1/{0} is {1} and the denominator is {2}".format(longestCycle(1000)[2], longestCycle(1000)[1], longestCycle(1000)[0]))
