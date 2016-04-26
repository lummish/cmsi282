def find_pour(cur_node, pour, node_set, pours_made):
	pours_made += [pour]
	if cur_node[1] == 2 or cur_node[2] == 2:
		pours_made.pop(0)
		return pours_made
	else:
		next_nodes = enumerate_children(cur_node, node_set, possible)
		if next_nodes == None or len(next_nodes) == 0:
			pours_made.pop() # remove pours that lead to invalid path
			return False
		for n in next_nodes:
			if find_pour(n[0], n[1], node_set, pours_made):
				return pours_made
		pours_made.pop() # remove pours that lead to invalid path
		return False

# Enumerates possible child nodes of current nodes
def enumerate_children(node, node_set, possible_moves):
	children = []
	for move in possible_moves:
		if is_valid(node, move):
			post_pour = pour(node, move) # status after pour
			if post_pour not in node_set: # only add to children if node not already in 
				children += [[post_pour, move]]
				node_set.add(post_pour)
	return children

def is_valid(node, move): # Checks if current pour string leads to valid result
	if 'E' in move:
		return True # Always able to empy container, if already empty, node will just be discarded
	if 'F' in move:
		return True # Always able to fill container, if already full, node will just be discarded
	if move == 'T47':
		if node[2] > 0 and node[1] < 7:
			return True
	if move == 'T410':
		if node[2] > 0 and node[0] < 10:
			return True
	if move == 'T74':
		if node[1] > 0 and node[2] < 4:
			return True
	if move == 'T710':
		if node[1] > 0 and node[0] < 10:
			return True
	if move == 'T104':
		if node[0] > 0 and node[2] < 4:
			return True
	if move == 'T107':
		if node[0] > 0 and node[1] < 7:
			return True

def remaining_cap(node, to_pitch): #calculates remaining capacity in chosen pitcher
	if to_pitch == 0:
		return 10 - node[0]
	if to_pitch == 1:
		return 7 - node[1]
	if to_pitch == 2:
		return 4 - node[2]

def pour(node, move):
	node_as_list = list(node)

	if move == 'E10':
		return 0, node[1], node[2]
	if move == 'E7':
		return node[0], 0, node[2]
	if move == 'E4':
		return node[0], node[1], 0
	if move == 'F10':
		return 10, node[1], node[2]
	if move == 'F7':
		return node[0], 7, node[2]
	if move == 'F4':
		return node[0], node[1], 4
	if move == 'T47':
		move_tup = (2,1)
	if move == 'T410':
		move_tup = (2,0)
	if move == 'T74':
		move_tup = (1,2)
	if move == 'T710':
		move_tup = (1,0)
	if move == 'T104':
		move_tup = (0,2)
	if move == 'T107':
		move_tup = (0, 1)

	from_pitch = move_tup[0]
	to_pitch = move_tup[1]

	remaining = remaining_cap(node_as_list, to_pitch)

	if remaining > node_as_list[from_pitch]: 
		node_as_list[to_pitch] += node_as_list[from_pitch]
		node_as_list[from_pitch] = 0
	else: 
		node_as_list[from_pitch] -= remaining
		node_as_list[to_pitch] += remaining
	
	return tuple(node_as_list)


possible = ['T47', 'T410', 'T74', 'T710', 'T104', 'T107', 'E7', 'E4', 'E10', 'F7', 'F4', 'F10'] # allowed pours
pours_made = []
node_set = set()
node_set.add((0,7,4))

print(find_pour((0,7,4), None, node_set, pours_made))
