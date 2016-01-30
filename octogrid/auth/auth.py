# -*- coding: utf-8 -*-

"""
octogrid.auth.auth

This module manages user authentication
"""

from ..settings import *
from os.path import abspath, expanduser, join
from getpass import getpass
from github3 import login, authorize

credentials_file_path = join(expanduser('~'), CREDENTIALS_FILE_NAME)
credentials_file = abspath(credentials_file_path)


def has_credentials_stored():
	""" Return 'auth token' string, if the user credentials are already stored
	"""

	try:
		with open(credentials_file, 'r') as f:
			token = f.readline().strip()
			id = f.readline().strip()

			return token
	except Exception, e:
		return False

def authenticate():
	""" Authenticate the user and store the 'token' for further use
		And return the authentication 'token'
	"""

	print LOGIN_INIT_MESSAGE

	username = raw_input('{0}: '.format(LOGIN_USER_MESSAGE))
	password = None

	while password is None:
		password = getpass('Password for {0}: '.format(username))

	gh = login(username, password=password)
	try:
		gh.user()
		instance = authorize(username, password, APP_SCOPE, APP_DESC, APP_URL)
	except Exception, e:
		raise e

	with open(credentials_file, 'w') as f:
		f.write(instance.token)

	return instance.token
