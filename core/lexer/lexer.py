from ..cogs import numbers, operators
from .tokens import Token

cogs = [
    numbers,
    operators,
]


class Lexer:
    def __init__(self, text: str, ignore=None):
        if ignore is None:
            self.ignore = [" ", "\t"]
        else:
            self.ignore = ignore

        self.tokens = []
        self.text = iter(text)
        self.pos = -1
        self.line = 0
        self.current = None

    def next(self):
        try:
            self.current = next(self.text)
            self.pos += 1

        except StopIteration:
            self.current = None
            self.tokens.append(Token("EOF", None))
