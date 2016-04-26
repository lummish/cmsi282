# Toal - CMSI 282 - Homework #4
Anthony Escobar & Harris Lummis


## 1. Dasgupta 3.8
```python
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
		return True # Always able to empy container
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


possible = ['T47', 'T410', 'T74', 'T710', 'T104', 'T107', 'E7', 'E4', 'E10'] # allowed pours
pours_made = []
node_set = set()
node_set.add((0,7,4))

print(find_pour((0,7,4), None, node_set, pours_made))
```
## 2. Dasgupta 4.1
|   | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| **0** | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| **1** | 0  |  1 |  ∞ |  ∞ | 4  |  8 |  ∞ |  ∞ |
| **2** | 0  | 1  |  3 | ∞  |  4 | 7  |  7 |  ∞ |
| **3** |  0 | 1  |  3 |  4 |  4 |  7 |  5 | ∞  |
| **4** |  0 | 1  |  3 | 4  |  4 |  7 |  5 |  8 |
| **5**|  0 | 1  |  3 | 4  | 4  |  7 |  5 |  8 |
| **6** |  0 | 1  |  3 | 4  | 4  |  6 |  5 |  6 |
| **7** |  0 | 1  |  3 | 4  | 4  | 6  |  5 |  6 |

## 3. Dasgupta 4.2
|  | S | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ 
| **1** | 0 | 7 | 11| 5 | 7 | 6 | 4 | 8 | 7 | 8
| **2** | 0 | 7 | 11| 5 | 7 | 6 | 4 | 8 | 7 | 7
| **3** | 0 | 7 | 11| 5 | 7 | 6 | 4 | 8 | 7 | 7

## 4. best_path.py
```python
from prims import Graph, Node
import sys, getopt

def main(argv):
	try:
		g = Graph()
		graph_string = str(argv[0])
		edge_array = graph_string.split('|')
		
		for e in edge_array:
			e_parsed = e.split(',')
			g.add_edge(e_parsed[2], e_parsed[1], e_parsed[0])

		shortest = {}
		best = {}

		node_set = g.get_nodes()
		node_set.insert(0, node_set.pop(node_set.index('s')))

		start = node_set[0]
		shortest[start] = 0
		best[start] = 0

		#set tentative values for remaining nodes
		for n in node_set[1:]:
			shortest[n] = [float('inf')]
			best[n] = [g.edge_count() + 1] #know that this is longer than any distinct sequence of edges in graph

		visited = [] #to store names of visited nodes


		for n in node_set:
			if n not in visited:
				cur_node = g.get_node(n)
				visited += [n]
				cur_dist = shortest[n]
				for adj in cur_node.get_adjacencies():
					if adj not in visited:
						adj_name = adj.get_name()
						#print(cur_node.get_weight(adj), cur_dist)
						if int(cur_node.get_weight(adj)) + cur_dist < shortest[adj_name]:
							shortest[adj_name] = int(cur_node.get_weight(adj)) + cur_dist
							best[adj_name] = best[n] + 1
						elif int(cur_node.get_weight(adj)) + cur_dist == shortest[adj_name]:
							shortest[adj_name] = int(cur_node.get_weight(adj)) + cur_dist
							if best[n] + 1 < best[adj_name]:
								best[adj_name] = best[n] + 1

		print(best)	

	except getopt.GetoptError:
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
```
## 5. prims.py
```python
import random
import Queue as Q
import sys, getopt

class UnconnectedGraphException(RuntimeError):
	def __init__(self, arg):
		self.args = arg

class Node:
	def __init__(self, name):
		self.name = name
		self.adjacent = {}

	#adds adjacent node
	def add_adjacent(self, adj, weight = 0):
		self.adjacent[adj] = weight
	#returns names of adjacent ndoes
	def get_adjacencies(self):
		return self.adjacent.keys()
	#returns name of node
	def get_name(self):
		return self.name
	#returns weight of edge between current and adj nodes
	def get_weight(self, adj):
		return self.adjacent[adj]


class Graph:
	def __init__(self):
		self.node_dict = {}
		self.num_nodes = 0
		self.num_edges = 0
	def __iter__(self):
		return iter(self.node_dict.values())
	def add_node(self, node):
		self.num_nodes += 1
		new_node = Node(node)
		self.node_dict[node] = new_node
		return new_node
	def get_node(self, n):
		if n in self.node_dict:
			return self.node_dict[n]
		else:
			return None
	def add_edge(self, weight, frm, to):
		if frm not in self.node_dict:
			self.add_node(frm)
		if to not in self.node_dict:
			self.add_node(to)

		self.node_dict[frm].add_adjacent(self.node_dict[to], weight)
		self.node_dict[to].add_adjacent(self.node_dict[frm], weight)
		self.num_edges += 1 # doesn't check if actual new edge was created
	def get_nodes(self):
		return self.node_dict.keys()
	def random_node(self):
		name = random.choice(self.node_dict.keys())
		return self.node_dict[name]
	def node_count(self):
		return self.num_nodes
	def edge_count(self):
		return self.num_edges


def prims(g):
	t = Graph()
	start = g.random_node()
	t.add_node(start.get_name())
	q = Q.PriorityQueue()
	adjacent_nodes = list(start.get_adjacencies())
	
	for n in adjacent_nodes:
		q.put((start.get_weight(n), start.get_name(), n.get_name())) #tuple with weight of edge, start, next node

	while t.node_count() < g.node_count():
		if q.empty():
			raise UnconnectedGraphException("") 
		
		(weight, frm, to) = q.get() #gets next closest node
		
		if to not in t.get_nodes():
			t.add_edge(weight, frm, to)
			to_node = g.get_node(to)

			possible_nodes = [x.get_name() for x in list(to_node.get_adjacencies())]
			current_nodes = list(t.get_nodes())
			for n in possible_nodes:
				if n not in current_nodes:
					q.put((to_node.get_weight(g.get_node(n)), to, n))
	return t

def output_set(st):
	out_str = ''
	for (frm, to, wt) in st:
		out_str += '{0},{1},{2}|'.format(frm, to, wt)
	return out_str[:-1]



def main(argv):
	try:
		g = Graph()
		graph_string = str(argv[0])
		edge_array = graph_string.split('|')
		
		for e in edge_array:
			e_parsed = e.split(',')
			g.add_edge(e_parsed[2], e_parsed[1], e_parsed[0])

		mst = prims(g)
		edge_set = set()

		for n in mst:
			for p in n.get_adjacencies():
				nid = n.get_name()
				pid = p.get_name()
				edge_set.add(tuple(sorted((nid, pid, n.get_weight(p)), reverse=True)))
		
		print(output_set(edge_set))
	except getopt.GetoptError:
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
```
## 6. subsetsum.py
```python
def subsetsum(sumset, gsum):
	for s in sumset:
		if s > gsum:
			sumset.remove(s) # elements larger than goal not part of solution
	if 0 not in sumset:
		sumset.insert(0,0) # need 0 element

	dp_grid = [[False for i in range(gsum + 1)] for j in range(len(sumset))]
	dp_grid[0][0] = True

	print(sumset)
	for i in range(1, len(sumset)):
		dp_grid[i][sumset[i]] = True

	for i in range(1, len(sumset)):
		for j in range(gsum + 1):
			if j - sumset[i] < 0:
				dp_grid[i][j] = dp_grid[i - 1][j]
			else:
				dp_grid[i][j] = dp_grid[i - 1][j] or dp_grid[i - 1][j - sumset[i]]

	return dp_grid[len(sumset) - 1][gsum]
```
## 7. Changer.java
```java
import java.util.Arrays;

public class Changer {
	private int[] denoms;
	public Changer(int[] denominations) {
		denoms = new int[denominations.length + 1]; //want to store zero as a denomination
		denoms[0] = 0;
		for (int i = 0; i < denominations.length; i++) {
			denoms[i + 1] = denominations[i];
		}
		Arrays.sort(denoms); //should make it simpler to minimize coin amounts in max_coins
	}

	public boolean can_make_change_for(int amount) { //need to check this method
		if (amount == 0) {
			return true;
		}
		boolean[][] grid = new boolean[denoms.length][amount + 1];
		grid[0][0] = true;

		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					if (j % denoms[i] == 0) {
						grid[i][j] = true;
					}
					else {
						grid[i][j] = grid[i - 1][j] || grid[i][j - denoms[i]];
					}
				}
			}
		}
		return grid[denoms.length - 1][amount];
	}

	public boolean can_make_change_using_each_coin_once(int amount) {
		if (amount == 0) {
			return true;
		}
		boolean[][] grid = new boolean[denoms.length][amount + 1];
		grid[0][0] = true;
		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					grid[i][j] = grid[i - 1][j] || grid[i - 1][j - denoms[i]];
				}
			}
		}
		
		return grid[denoms.length - 1][amount];
	}

	public boolean can_make_change_with_limited_coins(int amount, int max_coins) {
		if (amount == 0) {
			return true;
		}
		int[][] grid = new int[denoms.length][amount + 1];
		for (int i = 0; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				grid[i][j] = -1; //initialize to negative values for later checking
			}
		}
		grid[0][0] = 0;
		for (int i = 1; i < denoms.length; i++) {
			for (int j = 0; j <= amount; j++) {
				if (j - denoms[i] < 0) {
					grid[i][j] = grid[i - 1][j];
				}
				else {
					int add_coin = -1;
					int no_new_coin = -1;

					if (grid[i - 1][j - denoms[i]] >= 0) {
						if (grid[i][j - denoms[i]] >= 0) {
							//minimize number of coins (possible that current row number is min)
							add_coin = (grid[i - 1][j - denoms[i]] < grid[i][j - denoms[i]] ? 
									    grid[i - 1][j - denoms[i]] : grid[i][j - denoms[i]]); 
							add_coin++;
						}
						else {
							add_coin = grid[i - 1][j - denoms[i]] + 1;
						}
						
					} 
					if (j % denoms[i] == 0) {
						//if current coin can be added multiple times (greedy, will minimize coin amt)
						add_coin = j / denoms[i]; 
					} 
					else {
						no_new_coin = grid[i - 1][j];
					}

					if (add_coin >= 0 && no_new_coin >= 0) {
						//set grid position to minimum coin value for that sum
						grid[i][j] = (add_coin < no_new_coin ? add_coin : no_new_coin); 
					}

					else {
						//if one option is impossible, return the possible one
						grid[i][j] = (add_coin > no_new_coin ? add_coin : no_new_coin); 
					}
				}
			}
		}
		//print_int_grid(grid, amount, denoms); //for testing purposes 
		return grid[denoms.length - 1][amount] <= max_coins;
	}

	public static void print_boolean_grid(boolean[][] grid, int amount, int[] denoms) {
		for (int i = 0; i <= amount; i++) {
			if (i == 0) {
				System.out.print("   ");
			}
			System.out.print(i + " ");
		}
		System.out.println();
		for (int i = 0; i < denoms.length; i++) {
			System.out.print(i + ": ");
			for (int j = 0; j <= amount; j++) {
				if (grid[i][j]) {
					System.out.print("T ");	
				}
				else {
					System.out.print("F ");
				}
			}
			System.out.println();
		}
	}

	public static void print_int_grid(int[][] grid, int amount, int[] denoms) {
		for (int i = 0; i <= amount; i++) {
			if (i == 0) {
				System.out.print("   ");
			}
			System.out.format("%02d ", i);
		}
		System.out.println();
		for (int i = 0; i < denoms.length; i++) {
			System.out.print(i + ": ");
			for (int j = 0; j <= amount; j++) {
				System.out.format("%02d ", grid[i][j]);
			}
			System.out.println();
		}
	}
	public static void main(String[] args) {
		int[] denoms = {2,4,9};

		Changer c = new Changer(denoms);
		
		System.out.println(c.can_make_change_for(0));
		System.out.println(c.can_make_change_for(12));
		System.out.println(c.can_make_change_for(5));

		int[] denoms2 = {5,10};
		Changer c2 = new Changer(denoms2);

		c2.can_make_change_with_limited_coins(35, 6);
		c2.can_make_change_with_limited_coins(55, 6);
		c2.can_make_change_with_limited_coins(65, 6);
	}
}
```