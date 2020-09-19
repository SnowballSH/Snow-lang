from ..lexer.lexer import Lexer
from ..parser.parser import Parser
from ..interpreter.interpreter import Interpreter
from ..errors.pointer import point

import os
d = os.getcwd()

stdout = open(f"{d}\\snow.stdout", "w")

stderr = open(f"{d}\\snow.stderr", "w")


def run(file):
    with open(file, "r") as f:
        code = f.read()

    lexer = Lexer(code)
    res = lexer.lex()
    tokens, error = res

    if error:
        print(point(code, error.pos), file=stderr)
        print(f"<{file}> " + repr(error), file=stderr)
        return

    parser = Parser(tokens)
    res = parser.parse()
    nodes, error = res

    if error:
        print(point(code, error.pos), file=stderr)
        print(f"<{file}> " + repr(error), file=stderr)
        return

    inter = Interpreter(nodes)
    res = inter.run()
    res, error = res

    if error:
        print(point(code, error.pos), file=stderr)
        print(f"<{file}> " + repr(error), file=stderr)
        return

    # print(res)
