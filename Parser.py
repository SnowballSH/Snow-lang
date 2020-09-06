from nodes import *

COMPS = ("==", "!=", ">", "<", ">=", "<=")


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
            message = "Invalid Syntax: " + str(self.current[1])
        raise Exception(message)

    def parse(self):
        if self.current is None:
            return None

        res = []
        while self.current is not None:
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

            if crr == "let":
                self.next()
                if self.current[0] != "ID":
                    self.raise_syntax_error()

                name = self.current

                self.next()
                if self.current[0] != "SYM" or self.current[1] != "=":
                    self.raise_syntax_error()

                self.next()
                value = self.expr()

                return VarAssignNode(name, value)

            if crr == "def":
                self.next()
                if self.current[0] != "ID":
                    self.raise_syntax_error()
                name = self.current

                self.next()

                if self.current[0] == "BR" and self.current[1] == "(":
                    self.next()
                    paras = []
                    while self.current is not None and not (self.current[0] == "BR" and self.current[1] == ")"):
                        paras.append(self.current)
                        self.next()
                        if self.current[0] == "SYM" and self.current[1] == ",":
                            self.next()
                    if self.current[0] == "BR" and self.current[1] == ")":
                        self.next()
                        body = [self.expr()]
                        while self.current is not None and not (self.current[0] == "KW" and self.current[1] == "end"):
                            body.append(self.expr())
                        self.next()
                        return FuncAssignNode(name, paras, body)
                    else:
                        raise SyntaxError("Invalid Syntax")

            if crr == "import":
                self.next()
                if self.current[0] != "ID":
                    self.raise_syntax_error()
                name = self.current

                self.next()

                return ImportNode(name)

    def expr(self):
        kw = self.kw()
        if kw is not None:
            return kw

        res = self.term()

        while self.current is not None and self.current[0] == "OP" and self.current[1] in ("+", "-"):
            op = self.current
            self.next()
            res = OpNode(res, op, self.expr())

        while self.current is not None and self.current[0] == "SYM" and self.current[1] in COMPS:
            op = self.current
            self.next()
            res = CompNode(res, op, self.expr())

        return res

    def term(self):
        res = self.factor()
        while self.current is not None and self.current[0] == "OP" and self.current[1] in ("*", "/"):
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
                self.raise_syntax_error()

            self.next()
            return res

        if tok[0] == "NUMBER":
            self.next()
            return NumberNode(tok[1])

        if tok[0] == "STRING":
            self.next()
            return StringNode(tok[1])

        if self.current[0] == "ID":
            access = self.current
            self.next()
            if self.current is not None and self.current[0] == "BR" and self.current[1] == "(":
                self.next()
                res = []
                while self.current is not None and not (self.current[0] == "BR" and self.current[1] == ")"):
                    res.append(self.expr())
                    if self.current[0] == "SYM" and self.current[1] == ",":
                        self.next()
                if self.current[0] == "BR" and self.current[1] == ")":
                    self.next()
                    return FuncAccessNode(access, res)
                else:
                    raise SyntaxError("Invalid Syntax")
            else:
                return VarAccessNode(access)

        if (tok[0] == "OP" and tok[1] in ("+", "-")) or (tok[0] == "SYM" and tok[1] in ("!",)):
            self.next()
            return UnaryOpNode(tok, self.factor())

        self.raise_syntax_error()
