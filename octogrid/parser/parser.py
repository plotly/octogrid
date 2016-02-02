# -*- coding: utf-8 -*-

"""
octogrid.parser.parser

This module parses command-line arguments and take respective actions
"""

from ..collector.collector import collect_network
from ..generator.generator import generate_network


class ArgumentParser:
    def __init__(self, args):
        self.args = args

    def action(self):
        """ Invoke functions according to the supplied flags
        """

        user = self.args['--user'] if self.args['--user'] else None
        reset = True if self.args['--reset'] else False

        if self.args['export']:
            generate_network(user, reset)
        elif self.args['publish']:
            publish_network(user, reset)
