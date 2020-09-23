from .cogs import numbers, operators, identifier, symbols
from ..errors.error import *
from .tokens import Token

"""All cogs"""
cogs = [
    numbers,
    operators,
    identifier,
    symbols,
]


# Main Lexer class
class Lexer:
    def __init__(self, text: str):
        self.ignore = [" ", "\t"]
        self.new_line = ["\n"]

        self.tokens = []
        self.text = iter(text)
        self.pos = -1  # current position in the line
        self.line = 1  # current line
        self.tp = (self.line, self.pos)
        self.current = None

        self.next()

    def next(self):
        """
        Goes to the next character of the code
        :return: None
        """
        try:
            self.current = next(self.text)
            self.pos += 1
            self.tp = (self.line, self.pos)

        except StopIteration:  # If reaches the end
            self.current = None

    def lex(self):
        """
        Analyzes the code
        :return: list[tokens.Token]
        """

        while self.current is not None:
            valid = False

            # If new line, change line and reset pos, next()
            if self.current in self.new_line:
                self.line += 1
                self.pos = -1
                self.next()
                continue

            # If ignore, next()
            if self.current in self.ignore:
                self.next()
                continue

            if self.current == "#":
                while self.current is not None and self.current != "\n":
                    self.next()
                continue

            # get result from cogs
            for cog in cogs:
                res = cog.lex(self)
                if res is not None:
                    if res.type == "ERROR":
                        return None, res.value
                    self.tokens.append(res)
                    valid = True
                    break

            if valid:
                continue

            return None, SnowError.InvalidCharError(self.tp)

        self.tokens.append(Token("EOF", None, self.tp, self.tp))
        return self.tokens, None
