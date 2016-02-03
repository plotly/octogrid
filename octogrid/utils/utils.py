# -*- coding: utf-8 -*-

"""
octogrid.utils.utils

This module implements some utility functions required by the package 
"""

from json import loads
import colorlover as cl
from os.path import expanduser, isfile, join
import plotly.plotly as plotly
from random import choice, shuffle
from ..settings import *


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


def login_as_bot():
	"""
	Login as the bot account "octogrid", if user isn't authenticated on Plotly
	"""

	plotly_credentials_file = join(
    	join(expanduser('~'), PLOTLY_DIRECTORY), PLOTLY_CREDENTIALS_FILENAME)

	if isfile(plotly_credentials_file):
		with open(plotly_credentials_file, 'r') as f:
			credentials = loads(f.read())

		if (credentials['username'] == '' or credentials['api_key'] == ''):
			plotly.sign_in(BOT_USERNAME, BOT_API_KEY)
	else:
		plotly.sign_in(BOT_USERNAME, BOT_API_KEY)


def username_to_file(username):
	"""
	Return the network file name according to the username
	"""

	return '{0}.gml'.format(username)
