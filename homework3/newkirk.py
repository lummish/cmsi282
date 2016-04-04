schoolgirls = [''] * 105
girl_names = 'ABCDEFGHIJKLMNO'
LAST_SLOT = 104
from backtracker import backtracker

def place_from(slot):
	print(schoolgirls)
	for walker in girl_names:
		if can_walk(slot, walker):
			place_walker(slot, walker)
			if slot == LAST_SLOT:
				finish()
			else:
				place_from(slot+1)

def backtracker(toTest, possibleElements, solutionSize, isCorrect):
	print(toTest)
	if not isCorrect(toTest):
		return
	elif solutionSize == len(toTest):
		return toTest
	else:
		start = determine_first_to_test(toTest, len(toTest))
		end = determine_last_to_test(toTest, len(toTest))
		print(end)
		toTest += [start]
		cur_poss_idx = possibleElements.index(start)
		end_idx = possibleElements.index(end)
		current_branch_idx = len(toTest) - 1
		while True:
			toReturn = backtracker(toTest, possibleElements, solutionSize, isCorrect)
			if toReturn:
				return toReturn #return if toReturn is not None
			if cur_poss_idx == end_idx:
				break
			cur_poss_idx += 1
			toTest[current_branch_idx] = possibleElements[cur_poss_idx] #set current branch to next element in possibleElements
			toTest = toTest[:current_branch_idx + 1]

def determine_first_to_test(toTest, slot):
	if slot < 0:
		return 'A'
	start_of_day = 15 * (slot / 15)
	# Try A if first of day
	if slot % 15 == 0:
		return 'A'
	# For first row central elements
	if slot % 15 == 1:
		if slot > 1:
			prev_center = chr(ord(toTest[slot - 15]) + 1)
			left = chr(ord(toTest[slot - 1]) + 1)
			if prev_center > left:
				return prev_center
			else:
				return left
	# First column elements
	if slot % 3 == 0 and slot != start_of_day:
		prev = toTest[slot - 3]
		next_char = chr(ord(prev) + 1)
		if (next_char < 'P'): #ensure that incrementing character will not yeild letter larger than O
			return next_char
		else:
			return
	
	# others (all of which should have at least one element to their left)
	toReturn = chr(ord(toTest[slot - 1]) + 1)
	if toReturn > 'O':
		return 'O'
	else:
		return toReturn

def determine_last_to_test(toTest, slot):
	if slot > 14:
		print(toTest[-1], slot)
		if slot % 15 not in [2,5,8,11,14]:
			return 'L'
		else:
			return 'O'
	else:
		return 'O'


def isCorrect(toTest):
	if len(toTest) <= 1:
		return True
	# Check if most recent addition has already appeared in current day
	walker = toTest[-1]
	slot = len(toTest) - 1
	start_of_day_check = 15 * (slot / 15)
	end_of_day_check = slot
	for i in range(start_of_day_check, slot):
		if toTest[i] is walker:
			return False

	# Now check if walker has already been in the same row as its other row members
	row_num = slot % 15 / 3
	row_start = start_of_day_check + 3 * row_num
	row = toTest[row_start:row_start + 3]
	if len(row) == 1:
		return True
	for i in range(0, start_of_day_check, 3):
		comp_row = toTest[i:i+3]
		if len(set(comp_row + row)) < len(comp_row) + len(row) - 1:
			return False

	return True

print(backtracker([],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'], 105, isCorrect))

