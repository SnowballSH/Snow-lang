from ..tokens import Token
from .keywords import keywords

import string


def lex(self) -> Token or None:
    iden = ""
    start = self.tp
    end = self.tp

    while self.current is not None and self.current in string.ascii_letters + "_":
        iden += self.current
        end = self.tp
        self.next()

    if not iden:
        return

    if iden in keywords:
        return Token("KEYWORD", iden, start, end)
    else:
        return Token("ID", iden, start, end)
