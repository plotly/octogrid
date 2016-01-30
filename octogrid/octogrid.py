"""Octogrid: command line tool to export your GitHub network in GML format.

Usage:
	octogrid export [--user=<username>]
	octogrid -h | --help
	octogrid --version

Options:
	-h --help     Show this help screen
	--version     Show version
"""

from __init__ import __version__
from docopt import docopt
from parser.parser import ArgumentParser


def main():
	args = docopt(__doc__, version='Octogrid {0}'.format(__version__))
	parser = ArgumentParser(args)
	parser.action()


if __name__ == '__main__':
	main()
