from nodes import *

COMPS = ("==", "!=", ">", "<", ">=", "<=")


def not_none(current):
    return current is not None and current[0] != "EOF"


class Parser:
    def __init__(self, tokens: iter):
        self.tokens = iter(tokens)
        self.current = None
        self.next()

    def next(self):
        try:
            self.current = next(self.tokens)
        except StopIteration:
            self.current = None

    def raise_syntax_error(self, message=None):
        if message is None:
            message = str(self.current[1])
        raise SyntaxError(message)

    def parse(self):
        if self.current is None:
            return None

        res = []
        while not_none(self.current):
            res.append(self.expr())

        return res

    def kw(self):
        if self.current[0] == "KW":
            crr = self.current[1]
            if crr == "put":
                self.next()
                return PutNode(self.expr())

            if crr == "get":
                self.next()
                return GetNode(self.expr())

            if crr == "var":
                self.next()
                if self.current[0] != "ID":
                    self.raise_syntax_error(f"Expected identifier, but got '{self.current[1]}'")

                name = self.current

                self.next()
                if self.current[0] != "SYM" or self.current[1] != "=":
                    self.raise_syntax_error(f"Expected '=', but got '{self.current[1]}'")

                self.next()
                value = self.expr()

                return VarAssignNode(name, value)

            if crr == "def":
                self.next()

                name = ""
                if self.current[0] != "ID":
                    if self.current[0] == "OP" and self.current[1] == "*":
                        name = "<anonymous>"
                    else:

                        self.raise_syntax_error(f"Expected identifier, but got '{self.current[1]}'")
                else:
                    name = self.current

                self.next()

                if self.current[0] == "BR" and self.current[1] == "(":
                    self.next()
                    paras = []
                    while not_none(self.current) and not (self.current[0] == "BR" and self.current[1] == ")"):
                        paras.append(self.current)
                        self.next()
                        if self.current[0] == "SYM" and self.current[1] == ",":
                            self.next()
                    if self.current[0] == "BR" and self.current[1] == ")":
                        self.next()

                        if not (self.current[0] == "BR" and self.current[1] == "{"):
                            self.raise_syntax_error("Expected '{'"f", but got '{self.current[1]}'")
                        self.next()

                        body = [self.expr()]
                        while not_none(self.current) and not (self.current[0] == "BR" and self.current[1] == "}"):
                            body.append(self.expr())

                        if not (self.current[0] == "BR" and self.current[1] == "}"):
                            self.raise_syntax_error("Expected '}'"f", but got '{self.current[1]}'")
                        self.next()

                        if name != "<anonymous>":
                            return FuncAssignNode(name, paras, body)

                        return AnonFuncAssignNode(name, paras, body)

                    else:
                        self.raise_syntax_error(f"Expected closing parenthesis ')', but got '{self.current[1]}'")
                else:
                    self.raise_syntax_error(f"Expected '(', but got '{self.current[1]}'")

            if crr == "give":
                self.next()
                return GiveNode(self.expr())

            if crr == "import":
                self.next()
                if self.current[0] != "ID":
                    self.raise_syntax_error(f"Expected identifier, but got '{self.current[1]}'")
                name = self.current

                self.next()

                return ImportNode(name)

    def expr(self):
        kw = self.kw()
        if kw is not None:
            return kw

        res = self.term()

        while not_none(self.current) and self.current[0] == "OP" and self.current[1] in ("+", "-"):
            op = self.current
            self.next()
            ex = self.factor()
            res = OpNode(res, op, ex)

        while not_none(self.current) and self.current[0] == "SYM" and self.current[1] in COMPS:
            op = self.current
            self.next()
            res = CompNode(res, op, self.expr())

        return res

    def term(self):
        res = self.factor()
        while not_none(self.current) and self.current[0] == "OP" and self.current[1] in ("*", "/"):
            op = self.current
            self.next()
            res = OpNode(res, op, self.factor())

        return res

    def factor(self):
        tok = self.current

        if tok[0] == "BR" and tok[1] == "(":
            self.next()
            res = self.expr()
            if not (self.current[0] == "BR" and self.current[1] == ")"):
                self.raise_syntax_error(f"Expected closing parenthesis ')', but got '{self.current[1]}'")

            self.next()
            return res

        if tok[0] == "NUMBER":
            self.next()
            return NumberNode(tok[1])

        if tok[0] == "BOOL":
            self.next()
            return BoolNode(tok[1])

        if tok[0] == "NULL":
            self.next()
            return NullNode()

        if tok[0] == "STRING":
            self.next()
            return StringNode(tok[1])

        if self.current[0] == "ID":
            access = self.current
            self.next()
            if not_none(self.current) and self.current[0] == "BR" and self.current[1] == "(":
                self.next()
                res = []
                while not_none(self.current) and not (self.current[0] == "BR" and self.current[1] == ")"):
                    res.append(self.expr())
                    if self.current[0] == "SYM" and self.current[1] == ",":
                        self.next()
                if self.current[0] == "BR" and self.current[1] == ")":
                    self.next()
                    return FuncAccessNode(access, res)
                else:
                    self.raise_syntax_error(f"Expected closing parenthesis ')', but got '{self.current[1]}'")
            else:
                return VarAccessNode(access)

        if (tok[0] == "OP" and tok[1] in ("+", "-")) or (tok[0] == "SYM" and tok[1] in ("!",)):
            self.next()
            return UnaryOpNode(tok, self.factor())

        self.raise_syntax_error(f"Expected expression, got {self.current[1]}")
