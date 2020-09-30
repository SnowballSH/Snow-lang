from ..tokens import Token
from .keywords import kw as keywords

import string
import pathlib

d = pathlib.Path(__file__).parent.absolute()


def lex(self) -> Token or None:
    if self.current is not None and self.current in string.ascii_letters + "_":
        iden = ""
        start = self.tp
        end = self.tp

        while self.current is not None and self.current in string.ascii_letters + "_" + string.digits:
            iden += self.current
            end = self.tp
            self.next()

        if not iden:
            return

        if iden in keywords:
            return Token("KEYWORD", iden, start, end)
        else:
            return Token("ID", iden, start, end)
