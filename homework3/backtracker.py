#backtracker.py
def backtracker(toTest, possibleElements, solutionSize, isCorrect):
	if not isCorrect(toTest):
		return
	elif solutionSize == len(toTest):
		return toTest
	else:
		toTest += [possibleElements[0]]
		cur_poss_idx = 0
		current_branch_idx = len(toTest) - 1
		while True:
			toReturn = backtracker(toTest, possibleElements, solutionSize, isCorrect)
			if toReturn:
				return toReturn #return if toReturn is not None
			if cur_poss_idx == len(possibleElements) - 1:
				break
			cur_poss_idx += 1
			toTest[current_branch_idx] = possibleElements[cur_poss_idx] #set current branch to next element in possibleElements
			toTest = toTest[:current_branch_idx + 1]

