from ..tokens import Token

ref = {"(": "LPAREN", ")": "RPAREN", "=": "EQ", "==": "DBEQ", ":=": "WALRUS", ":": "COLON", "<": "LT", ">": "GT",
       "<-": "LARROW", "->": "RARROW", "<=": "LTEQ", ">=": "GTEQ", "!": "NOT", "!=": "NOTEQ", "{": "LCURLY",
       "}": "RCURLY", ",": "COMMA"}


def make_sym(self, sym):
    self.next()
    end = self.tp
    if self.current is None:
        return sym, end
    if sym + self.current in ref.keys():
        crr = self.current
        return make_sym(self, sym + crr)
    else:
        return sym, end


def lex(self) -> Token:
    if self.current in ref.keys():
        start = self.tp
        sym = self.current

        sym, end = make_sym(self, sym)
        sym_type = ref[sym]

        return Token(sym_type, sym, start, end)
