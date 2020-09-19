from ..tokens import Token
from ...errors.error import SnowError


def get_num(self) -> Token:
    """
    Gets the num
    :param self: Lexer
    :return: an integer
    """
    num = ""
    dot = False

    start = self.tp
    end = self.tp

    while self.current is not None and (self.current.isdigit() or self.current == "."):
        if self.current == ".":
            # Detect for float
            if dot:
                return Token("ERROR", SnowError.SyntaxError(self.tp), start, self.tp)

            dot = not dot
            if not dot:
                self.next()
                break
        num += self.current
        end = self.tp
        self.next()

    return Token(*("FLOAT", float(num)) if dot else ("INT", int(num)), start, end) if num else None


def lex(self) -> Token:
    res = get_num(self)
    return res
