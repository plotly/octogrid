"""Octogrid: command line tool to export your GitHub network in GML format.

Usage:
	octogrid export [--user=<username>]
	octogrid -h | --help
	octogrid --version

Options:
	-h --help     Show this help screen
	--version     Show version
"""

from docopt import docopt
from github3 import login
from getpass import getpass
from os import expanduser, join


# @TODO: import version from init file
def main():
	args = docopt(__doc__, version='Octogrid 0.0.0')
	print args


if __name__ == '__main__':
	main()