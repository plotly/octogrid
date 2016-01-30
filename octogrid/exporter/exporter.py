# -*- coding: utf-8 -*-

"""
octogrid.exporter.exporter

This module helps collecting the network for a user
"""


from github3 import login
from ..auth.auth import has_credentials_stored, authenticate
from ..builder.builder import generate_gml


def collect_token():
	""" Collect the authentication token from local storage
	"""

	# @TODO: returns 422 if a token is already there for the app
	previous_token = has_credentials_stored()
	if not previous_token:
		previous_token = authenticate()

	return previous_token

def export_network(user=None):
	""" Assemble the network connections for a given user
	"""

	token = collect_token()
	print token

	try:
		gh = login(token=token)
		root_user = gh.user(user)
	except Exception, e:
		# Failed to login using the token, github3.models.GitHubError
		raise e

	graph_nodes = []
	graph_edges = []

	username = user if user is not None else root_user.name
	graph_nodes.append(username)

	# @TODO: take care of the 'rate limit exceeding' if imposed
	try:
		for person in gh.iter_following(username):
			graph_nodes.append(str(person))
			graph_edges.append((root_user.login, str(person)))

		for i in range(1, root_user.following):
			user = gh.user(graph_nodes[i])
			user_following_edges = [(user.login, str(person)) for person in gh.iter_following(user) if str(person) in graph_nodes]
			graph_edges += user_following_edges
	except Exception, e:
		raise e

	generate_gml(username, graph_nodes, graph_edges)
