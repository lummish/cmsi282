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



