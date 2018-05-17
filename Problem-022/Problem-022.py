'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import re
from itertools import count
from string import ascii_uppercase


def letter_indexes(text):
	# Create a dictionary of letters and it's alphabetical value
    letter_mapping = dict(zip(ascii_uppercase, count(1)))
    # Iterate through each character in text and then get the index of it in the dictionary (created above)
    indexes = [letter_mapping[letter] for letter in text if letter in letter_mapping]
    return indexes

# Add in data
file = open('p022_names.txt', 'r')

rawNames = []
for word in file:
	for i in word.split(","):
		rawNames.append(i)

# Get string between quotations and put them in a list
sortedNames = []
for i in range(len(rawNames)):
	sortedNames.append(re.findall('"([^"]*)"', rawNames[i])[0])
# Sort names list alphbetically.
sortedNames = sorted(sortedNames)

totalScore = 0
indexSum = 0
nameIndex = 0
for name in sortedNames:
	indexSum = sum(letter_indexes(name))
	# Plus one since it is indexed from zero
	nameIndex = sortedNames.index(name) + 1
	totalScore += (indexSum * nameIndex)

print(totalScore)
