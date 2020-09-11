WHITESPACE = [" ", "\t", "\n"]
OPERATORS = "+-*/"
BRACKETS = "(){}"
SYMBOLS = ("=", "!", ">", "<", ",", "?")
BOOLS = ("True", "False")
NULLTYPE = ("Null",)
KEYWORDS = ["put", "get", "var", "def", "give", "import",
            "if", "else"]


class Lexer:
    def __init__(self, data: str):
        data += "\n"
        self.data = iter(data)
        self.current = None
        self.next()

    def next(self):
        try:
            self.current = next(self.data)
        except StopIteration:
            self.current = None

    def lex(self):
        while self.current is not None:
            if self.current == "#":
                while True:
                    self.next()
                    if self.current == "\n":
                        self.next()
                        break
            elif self.current in WHITESPACE:
                self.next()
            elif self.current.isalpha() or self.current == "_":
                yield self.get_id()
            elif self.current == '"':
                yield self.get_str()
            elif self.current.isdigit() or self.current == ".":
                yield self.get_num()
            elif self.current in OPERATORS:
                yield self.get_op()
            elif self.current in BRACKETS:
                yield self.get_br()
            elif self.current in SYMBOLS:
                a = self.current
                a = self.get_comp(a)
                yield "SYM", a
            else:
                raise SyntaxError("Invalid Character: " + self.current)
        yield "EOF", "None"

    def get_id(self):
        alphas = self.current
        self.next()
        while self.current is not None and (self.current.isalnum() or self.current == "_"):
            alphas += self.current
            self.next()

        if alphas in KEYWORDS:
            return "KW", alphas

        elif alphas in BOOLS:
            return "BOOL", alphas
        elif alphas in NULLTYPE:
            return "NULL", alphas

        return "ID", alphas

    def get_num(self):
        nums = self.current
        dot = nums == "."
        self.next()
        while self.current is not None and (self.current.isdigit() or self.current == "."):
            if self.current == ".":
                dot = not dot
                if not dot:
                    self.next()
                    break
            nums += self.current
            self.next()

        return "NUMBER", float(nums) if dot else int(nums)

    def get_str(self):
        string = ""
        self.next()
        while self.current is not None and self.current != '"':
            string += self.current
            self.next()

        if self.current != '"':
            raise SyntaxError("Invalid Syntax: Expected to find '\"'")

        self.next()
        return "STRING", string

    def get_comp(self, sym):
        if sym == "=":
            self.next()
            if self.current == ">":
                self.next()
                return "=>"
            if self.current == "=":
                self.next()
                return sym + "="
            else:
                return sym
        self.next()
        if self.current == "=":
            self.next()
            return sym + "="
        else:
            return sym

    def get_op(self):
        op = self.current
        self.next()
        return "OP", op

    def get_br(self):
        br = self.current
        self.next()
        return "BR", br
