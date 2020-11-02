from argparse import ArgumentParser
from inspy_logger import LEVELS as LOG_LEVELS
from MTGArenaCompanion import MTGACApp
from pathlib import Path

class ArgParser(ArgumentParser, MTGACApp):
    arguments = None

    def parse(self):
        self.add_argument('-l', '--log-level',
                          action='store',
                          choices=LOG_LEVELS,
                          default='info',
                          help='The level at which you\'d like the program to output log messages.')

        self.arguments = self.parse_args()
