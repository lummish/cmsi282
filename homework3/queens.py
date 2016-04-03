# nQueens.py
from backtracker import backtracker

def isCorrect(toTest):
	if len(toTest) > len(set(toTest)): # return false if not all rows unique
			return False
	for i in range(len(toTest) - 1):
		diagonal_distance = 1
		for j in range(i + 1, len(toTest)):
			if (toTest[j] == toTest[i] + diagonal_distance or
				toTest[j] == toTest[i] - diagonal_distance):			
				return False
			diagonal_distance += 1
	return True
