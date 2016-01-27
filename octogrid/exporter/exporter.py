# -*- coding: utf-8 -*-

"""
octogrid.exporter.exporter

This module helps collecting the network for a user
"""

from ..auth.auth import has_credentials_stored, authenticate


def export_network(user=None):
	""" Assemble the network connections for a given user
	"""

	previous_token = has_credentials_stored()
	if previous_token:
		pass
	else:
		authenticate()