# -*- coding: utf-8 -*-

"""
octogrid.builder.builder

This module helps in generating a GML file from the graph content
"""

FILE_PREFIX = 'graph\n[\n'
FILE_SUFFIX = ']'
NODE_PREFIX = '\tnode\n\t[\n'
NODE_SUFFIX = '\t]\n'
EDGE_PREFIX = '\tedge\n\t[\n'
EDGE_SUFFIX = '\t]\n'


def format_node(id, label):
	""" Return the formatted string to represent a node
	"""

	return NODE_PREFIX + id + label + NODE_SUFFIX

def format_edge(source, target):
	""" Return the formatted string to represent an edge
	"""

	return EDGE_PREFIX + source + target + EDGE_SUFFIX

def generate_gml(username, nodes, edges):
	""" Generate a GML format file representing the given graph attributes
	"""

	# file segment that represents all the nodes in graph
	node_content = ""
	for i in range(len(nodes)):
		node_id = "\t\tid %d\n" % (i + 1)
		node_label = "\t\tlabel \"%s\"\n" % (nodes[i])

		node_content += format_node(node_id, node_label)

	# file segment that represents all the edges in graph
	edge_content = ""
	for i in range(len(edges)):
		edge = edges[i]

		edge_source = "\t\tsource %d\n" % (nodes.index(edge[0]) + 1)
		edge_target = "\t\ttarget %d\n" % (nodes.index(edge[1]) + 1)

		edge_content += format_edge(edge_source, edge_target)

	# prepared file content
	content = FILE_PREFIX + node_content + edge_content + FILE_SUFFIX

	with open('{0}.gml'.format(username), 'w') as f:
		f.write(content)