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
from parser.parser import ArgumentParser


# @TODO: import version from init file
def main():
	args = docopt(__doc__, version='Octogrid 0.0.0')
	parser = ArgumentParser(args)
	parser.action()


if __name__ == '__main__':
	main()
