#backtracker.py
def backtracker(toTest, maxCandVal, solutionSize, isCorrect):
	if not isCorrect(toTest):
		return
	elif solutionSize == len(toTest):
		return toTest
	else:
		toTest += [0]
		current_branch_idx = len(toTest) - 1
		while toTest[-1] < maxCandVal:
			toReturn = backtracker(toTest, maxCandVal, solutionSize, isCorrect)
			if toReturn:
				return toReturn
			toTest[current_branch_idx] += 1
			toTest = toTest[:current_branch_idx + 1]
	 
def backtrackerNew(toTest, possibleElements, solutionSize, isCorrect):
	if not isCorrect(toTest):
		return
	elif solutionSize == len(toTest):
		return toTest
	else:
		toTest += [possibleElements[0]]
		cur_poss_idx = 0
		current_branch_idx = len(toTest) - 1
		while True:
			toReturn = backtrackerNew(toTest, possibleElements, solutionSize, isCorrect)
			if toReturn:
				return toReturn #return if toReturn is not None
			if cur_poss_idx == len(possibleElements) - 1:
				break
			cur_poss_idx += 1
			toTest[current_branch_idx] = possibleElements[cur_poss_idx] #set current branch to next element in possibleElements
			toTest = toTest[:current_branch_idx + 1]

def isQCorrect(toTest):
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

def isNEASCorrect(toTest):
	if len(toTest) > 1:
		if toTest[-1] == toTest[-2]:
			return False
		compSize = 2
		while(compSize <= len(toTest) / 2): #max substring will be half size of test array
			if toTest[-compSize:] == toTest[-compSize * 2:-compSize]:
				return False
			compSize += 1
	return True


print(backtracker([], 8, 8, isQCorrect))
print(backtrackerNew([], [0,1,2,3,4,5,6,7], 8, isQCorrect))
print("".join(str(i) for i in backtrackerNew([], [0,1,2], 50, isNEASCorrect)))
print("01020120210120102012021020102101201020120210120102")
