from itertools import permutations


# Permutations method already generates permutations in lexicographic order.
listOfPermutations = list(permutations([0,1,2,3,4,5,6,7,8,9]))

# Index 999999 to retrieve millionth permutation
print(listOfPermutations[999999])




