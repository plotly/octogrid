# -*- coding: utf-8 -*-

"""
octogrid.parser.parser

This module manages the local cache storage preventing API resources 
"""

from ..settings import *
from shutil import copyfile
from os import getcwd
from os.path import abspath, expanduser, isfile, join


def cache_file(file_name):
	"""
	Cache a given file for further use (by storing them on disk)
	"""

	remote_file_path = join(join(expanduser('~'), DIRECTORY), file_name)

	try:
		copyfile(file_name, remote_file_path)
	except Exception, e:
		raise e


def copy_file(file_name):
	"""
	Copy a given file from the cache storage
	"""

	remote_file_path = join(join(expanduser('~'), DIRECTORY), file_name)
	current_path = join(getcwd(), file_name)

	try:
		copyfile(remote_file_path, current_path)
	except Exception, e:
		raise e


def is_cached(file_name):
	"""
	Check if a given file is available in the cache or not
	"""

	gml_file_path = join(join(expanduser('~'), DIRECTORY), file_name)

	return isfile(gml_file_path)
