import networkx as nx
g = nx.Graph()
g.add_node((0,7,4))


possible = ['T47', 'T410', 'T74', 'T710', 'T104', 'T107', 'E7', 'E4', 'E10']
pours_made = []
node_set = set()
node_set.add((0,7,4))

def find_pour(cur_node, node_set, pours_made):
	print('pours_made: ', pours_made)
	pours_made += [cur_node]
	if cur_node[1] == 2 or cur_node[2] == 2:
		return True
	else:
		next_nodes = enumerate_children(cur_node, node_set, possible)
		#print(next_nodes)
		if next_nodes == None or len(next_nodes) == 0:
			pours_made.pop()
			return False
		for n in next_nodes:
			if find_pour(n, node_set, pours_made):
				return True
		return False

def enumerate_children(node, node_set, possible_moves):
	children = []
	for move in possible_moves:
		if is_valid(node, move):
			post_pour = pour(node, move)
			if post_pour not in node_set:
				children += [post_pour]
				node_set.add(post_pour)
	return children

def is_valid(node, move):
	if 'E' in move:
		return True
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

def remaining_cap(node, to_pitch):
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
	#print(remaining)
	if remaining > node_as_list[from_pitch]:
		node_as_list[to_pitch] += node_as_list[from_pitch]
		node_as_list[from_pitch] = 0
	elif node_as_list[from_pitch] >= remaining: #probably can just change to else
		node_as_list[from_pitch] -= remaining
		node_as_list[to_pitch] += remaining


	return tuple(node_as_list)

print(find_pour((0,7,4), node_set, pours_made))
#print(pour((4,7,0), 'T710'))