from ..tokens import Token

ref = {"(": "LPAREN", ")": "RPAREN", "=": "EQ", "==": "DBEQ", ":=": "WALRUS", ":": "COLON"}


def make_eq(self):
    self.next()
    end = self.tp
    if self.current == "=":
        self.next()
        return "==", end
    else:
        self.next()
        return "=", end


def make_colon(self):
    self.next()
    end = self.tp
    if self.current == "=":
        self.next()
        return ":=", end
    else:
        self.next()
        return ":", end


def lex(self) -> Token:
    if self.current in ref.keys():
        start = self.tp
        sym = self.current
        if sym == "=":
            sym, end = make_eq(self)
        elif sym == ":":
            sym, end = make_colon(self)
        else:
            end = self.tp
            self.next()
        sym_type = ref[sym]

        return Token(sym_type, sym, start, end)
