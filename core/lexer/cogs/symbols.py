from ..tokens import Token

ref = {"(": "LPAREN", ")": "RPAREN"}


def lex(self) -> Token:
    if self.current in ref.keys():
        start = self.tp
        sym = self.current
        sym_type = ref[sym]
        end = self.tp

        self.next()
        return Token(sym_type, sym, start, end)
