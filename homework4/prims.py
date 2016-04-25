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
	def get_nodes(self):
		return self.node_dict.keys()
	def random_node(self):
		name = random.choice(self.node_dict.keys())
		return self.node_dict[name]
	def node_count(self):
		return self.num_nodes


def prims(g):
	t = Graph()
	start = g.random_node()
	t.add_node(start.get_name())
	q = Q.PriorityQueue()
	adjacent_nodes = list(start.get_adjacencies())
	
	for n in adjacent_nodes:
		#print ((start.get_weight(n), start.get_name(), n.get_name()))
		# print((start.get_weight(n), start.get_name(), n.get_name()))
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

'''
g = Graph()


g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')
g.add_node('g')

g.add_edge(5,'a','c')
g.add_edge(3,'c','d')
g.add_edge(1,'d','f')
g.add_edge(7,'f','b')
g.add_edge(1,'b','a')
g.add_edge(2,'c','e')
g.add_edge(4,'d','e')
g.add_edge(3,'f','e')
g.add_edge(6,'e','b')

mst = prims(g)

for n in mst:
	for p in n.get_adjacencies():
		nid = n.get_name()
		pid = p.get_name()
		print '( %s, %s, %3d)' % (nid, pid, n.get_weight(p))

'''
