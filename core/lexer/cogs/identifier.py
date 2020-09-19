from ..tokens import Token

import json
import string
import pathlib
d = pathlib.Path(__file__).parent.absolute()


with open(f"{d}\\keywords.json", "r") as f:
    keywords = json.load(f)


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
