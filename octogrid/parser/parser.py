# -*- coding: utf-8 -*-

"""
octogrid.parser.parser

This module parses command-line arguments and take respective actions
"""

from ..exporter.exporter import export_network

class ArgumentParser:
    def __init__(self, args):
        self.args = args

    def action(self):
        """ Invoke functions according to the supplied flags
        """

        if self.args['export']:
            user = None
            if self.args['--user']:
                user = self.args['--user']

            export_network(user)