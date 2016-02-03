"""Octogrid: GitHub following network visualizer for Humans.

Usage:
	octogrid generate [--reset] [--user=<username>]
	octogrid publish [--reset] [--user=<username>]
	octogrid -h | --help
	octogrid --version

Options:
	--reset       Clear the cache for given username
	--version     Show version
	-h --help     Show this help screen
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
