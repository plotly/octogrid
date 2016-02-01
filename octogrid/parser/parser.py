# -*- coding: utf-8 -*-

"""
octogrid.parser.parser

This module parses command-line arguments and take respective actions
"""

from ..exporter.exporter import export_network
from ..publisher.publisher import publish_network

class ArgumentParser:
    def __init__(self, args):
        self.args = args

    def action(self):
        """ Invoke functions according to the supplied flags
        """

        user = None
        if self.args['--user']:
            user = self.args['--user']

        if self.args['export']:
            export_network(user)
        elif self.args['publish']:
            publish_network(user)