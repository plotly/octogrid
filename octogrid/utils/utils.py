# -*- coding: utf-8 -*-

"""
octogrid.utils.utils

This module implements some utility functions required by the package 
"""

import colorlover as cl
from random import choice, shuffle


def community_colors(n):
	"""
	Returns a list of visually separable colors according to total communities
	"""

	if (n > 0):
		colors = cl.scales['12']['qual']['Paired']
		shuffle(colors)

		return colors[:n]
	else:
		return choice(cl.scales['12']['qual']['Paired'])


def username_to_file(username):
	"""
	Return the network file name according to the username
	"""

	return '{0}.gml'.format(username)
