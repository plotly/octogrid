# -*- coding: utf-8 -*-

"""
octogrid.builder.builder

This module helps in generating a GML file from the graph content
"""

from ..store.store import cache_file, copy_file
from ..utils.utils import username_to_file

FILE_PREFIX = 'graph\n[\n'
FILE_SUFFIX = ']\n'
NODE_PREFIX = '\tnode\n\t[\n'
NODE_SUFFIX = '\t]\n'
EDGE_PREFIX = '\tedge\n\t[\n'
EDGE_SUFFIX = '\t]\n'
SIGNATURE = 'Creator "octogrid [https://git.io/vzhM0]"\n'


def format_node(id, label):
    """
    Return the formatted string to represent a node
    """

    return NODE_PREFIX + id + label + NODE_SUFFIX


def format_edge(source, target):
    """
    Return the formatted string to represent an edge
    """

    return EDGE_PREFIX + source + target + EDGE_SUFFIX


def format_content(node, edge):
    """
    Return the formatted GML file content
    """

    return SIGNATURE + FILE_PREFIX + node + edge + FILE_SUFFIX


def reuse_gml(username):
    """
    Use the cached copy for this username
    """

    copy_file(username_to_file(username))


def generate_gml(username, nodes, edges, cache=False):
    """
    Generate a GML format file representing the given graph attributes
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

    # formatted file content
    content = format_content(node_content, edge_content)

    with open(username_to_file(username), 'w') as f:
        f.write(content)

    # save the file for further use
    if cache:
    	cache_file(username_to_file(username))
