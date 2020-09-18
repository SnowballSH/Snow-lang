def get_num(self):
    """
    Gets the num
    :param self: Lexer
    :return: an integer
    """
    num = ""
    while self.current is not None and self.current.isdigit():
        num += self.current
        self.next()

    return int(num) if num else None


def lex(self):
    res = get_num(self)
    return res
