from ..tokens import Token

ref = {"+": "ADD", "-": "MIN", "*": "MUL", "/": "DIV"}


def lex(self) -> Token:
    if self.current in ref.keys():
        start = self.tp
        op = self.current
        op_type = ref[op]
        end = self.tp

        self.next()
        return Token(op_type, op, start, end)
