#kirkman.py
from backtracker import backtracker
'''
Solution will take the form:
[[[0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11],
  [12,13,14]],
 [[next day matrix],...]
'''
def isCorrect(solution):
	newestRow = solution[-1][-1]
	newestElement = solution[-1][-1][-1]
	for row in solution[-1][:-2]: # make sure that number has not appeared in current day
		if newestElement in row:
			return False
	if len(newestRow) > 1: # tests for correctness when two elements are in the same row
		for day in solution:
			for row in day:
				# If there are two or more non unique elements relative to another row, 
				# must not be a viable solution
				if len(set(row + newestRow)) < len(row) + len(newestRow) - 1:
					return False
		return True




