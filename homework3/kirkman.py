# kirkiter.py
import itertools



def backtracker(toTest, possibleElements, solutionSize, isCorrect):
	if not isCorrect(toTest):
		return
	elif solutionSize == len(toTest):
		return toTest
	else:
		toTest += [possibleElements[0]]
		cur_poss_idx = first_possible(toTest)
		last_possible_idx = last_possible(toTest)
		current_branch_idx = len(toTest) - 1
		while True:
			toReturn = backtracker(toTest, possibleElements, solutionSize, isCorrect)
			if toReturn:
				return toReturn #return if toReturn is not None
			if cur_poss_idx > last_possible_idx:
				break
			cur_poss_idx += 1
			toTest[current_branch_idx] = possibleElements[cur_poss_idx] #set current branch to next element in possibleElements
			toTest = toTest[:current_branch_idx + 1]

girl_names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
possible = list(itertools.combinations(girl_names, 3))

def first_possible(toTest):
	if len(toTest) < 5:
		return possible.index(('A', 'B', 'C'))
	#for central first elements
	if len(toTest) % 5 == 1:
		next_first_center = chr(ord(toTest[-6][1]) + 1)
		final_char = chr(ord(next_first_center) + 1)
		return possible.index(('A', next_first_center, final_char))
	elif len(toTest) % 5 == 2:
		return possible.index(('B', 'C', 'D'))
	elif len(toTest) % 5 == 3:
		return possible.index(('C', 'D', 'E'))
	else:
		char_above_ord = ord(toTest[-2][0])
		return possible.index((chr(char_above_ord + 1), chr(char_above_ord + 2),
			chr(char_above_ord + 3)))

def last_possible(toTest):
	num_days = (len(toTest) / 5) + 1
	if len(toTest) <= 5:
		return 455
	#first row central elements
	if len(toTest) % 5 == 1:
		middle = chr(ord('H') + num_days) # may need to reduce by 1
		return possible.index(('A', middle, 'O'))
	elif len(toTest) % 5 == 2:
		return possible.index(('B', 'L', 'O'))		
	elif len(toTest) % 5 == 3:
		return possible.index(('C', 'L', 'O'))
	else:
		return possible.index(('K','L','O'))

def isCorrect(toTest):
	if len(toTest) <= 1:
		return True
	# check if element appears twice in day
	day_num = (len(toTest) - 1) / 5
	new_row_lst = list(toTest[-1])
	for i in range(5 * day_num, len(toTest) - 1):
		for name in new_row_lst:
			if name in toTest[i]:
				return False

	# check if two elements have already appeared together
	for i in range(len(toTest) - 1): # don't need to check newest one
		if len(set(list(toTest[i]) + new_row_lst)) < 5:
			return False

	return True
