"""
Author: Scott C Gramig
Program: Finds multiple duplicates in an array of 
	100 randomly generated integers valued 0 to 50
	and displays the top 5 frequencies
"""

import random
import collections


numList = []
cnt = collections.Counter()

# generate list of rand numbers
for n in range(0, 100):
	numList.append(random.randint(0, 50))

# popular collections.Counter to get frequencies
cnt.update(numList)

print "\n\nList of numbers: ", numList

# freq can be used for future manipulation
freq = cnt.most_common(5)
print "\n\nTop 5 frequencies in list: ", freq
