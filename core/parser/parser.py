from .nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def next(self):
        next(self.tokens)
