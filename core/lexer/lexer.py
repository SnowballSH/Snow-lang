from ..cogs import numbers, operators
from .tokens import Token

"""All cogs"""
cogs = [
    numbers,
    operators,
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
            self.tokens.append(Token("EOF", None, self.tp, self.tp))

    def lex(self):
        """
        Analyzes the code
        :return: list[tokens.Token]
        """

        tokens = []

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

            # get result from cogs
            for cog in cogs:
                res = cog.lex(self)
                if res is not None:
                    if res.type == "ERROR":
                        return None, res.value
                    tokens.append(res)
                    valid = True
                    break

            if valid:
                continue

            raise Exception(f"Invalid character: {self.current}")

        return tokens, None
