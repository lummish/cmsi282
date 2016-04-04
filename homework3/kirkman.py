#kirkman.py
'''
Solution will take the form:
[[[0,1,2],
  [3,4,5],
  [6,7,8],
  [9,10,11],
  [12,13,14]],
 [[next day matrix],...]
'''
def kirkmanBacktracker(toTest, total_days, isCorrect):
	print(toTest)
	if not isCorrect(toTest):
		return
	elif (total_days == len(toTest) and 5 == len(toTest[-1]) and 
		  3 == len(toTest[-1][-1])):
		return toTest
	else:
		# -1 is used as a placeholder element that will simplify the process of 
		# getting the current_branch_idx
		if len(toTest) == 0 or (len(toTest[-1]) == 5 and len(toTest[-1][-1]) == 3): 
			print("new day")
			# if there are no days yet or a new day must be added
			day_idx = len(toTest)
			row_idx = 0
			girl_idx = 0

			toTest += [[[0]]] # begin new 2d array

		else:
			if len(toTest[-1][-1]) == 3 and len(toTest[-1]) < 5:
				# if a new row must be added to the current day, add one
				day_idx = len(toTest) - 1
				row_idx = len(toTest[-1])
				girl_idx = 0

				toTest[-1] += [[0]]	
			else:
				# if there is space remaining in the current row, add an element
				day_idx = len(toTest) - 1
				row_idx = len(toTest[-1]) - 1
				girl_idx = len(toTest[-1][-1])

				toTest[-1][-1] += [0] # maybe want to make sure its not in the current day set

		cur_schoolgirl = 0 

		while True:
			print("totest", toTest)
			toReturn = kirkmanBacktracker(toTest, total_days, isCorrect)
			print("new totest", toTest)
			if toReturn:
				return toReturn #return if toReturn is not None
			if cur_schoolgirl == 15: #hopefully dont get here
				break
			# if path fails, go to neighbor path and trim remaining from array
			cur_schoolgirl += 1
			toTest[day_idx][row_idx][girl_idx] = cur_schoolgirl #set current branch to next element in possibleElements
			print("totest new schoolgirl", toTest)
			print("cur_schoolgirl", cur_schoolgirl)
			print("indices: ", day_idx, row_idx, girl_idx)
			toTest = toTest[:day_idx + 2][:row_idx + 1][:girl_idx + 1] # why is this broken?????
			print("totest", toTest)


def Correct(solution):
	if len(solution) == 0:
		return True
	elif len(solution[-1][-1]) < 1:
		return True
	newestRow = solution[-1][-1]
	if len(set(newestRow)) < len(newestRow):
		print("duplicate in same row")
		return False
	newestElement = solution[-1][-1][-1]
	print("solution", solution[-1][:-1])
	for row in solution[-1][:-1]: # make sure that number has not appeared in current day		
		if newestElement in row:
			return False
	if len(newestRow) > 1: # tests for correctness ONLY when two elements are in the same row
		for day in solution[:-1]: #wont need to test current day
			for row in day:
				# If there are two or more non unique elements relative to another row, 
				# must not be a viable solution (i.e. if two elements have already appeared
				# in the same row, discard current solution)
				if len(set(row + newestRow)) < len(row) + len(newestRow) - 1:
					print("duplicate")
					return False
	return True

print(kirkmanBacktracker([], 7, Correct))