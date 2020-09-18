from ..lexer.tokens import Token


def get_num(self) -> Token:
    """
    Gets the num
    :param self: Lexer
    :return: an integer
    """
    num = ""
    while self.current is not None and self.current.isdigit():
        num += self.current
        self.next()

    return Token("int", int(num)) if num else None


def lex(self) -> Token:
    res = get_num(self)
    return res
