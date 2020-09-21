from ..lexer.lexer import Lexer
from ..parser.parser import Parser
from ..interpreter.interpreter import Interpreter
from ..errors.pointer import point

import os
import sys

d = os.getcwd()


def run_f(file, stdout, stderr):
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

    inter = Interpreter(nodes, stdout)
    res = inter.run()
    res, error = res

    if error:
        print(point(code, error.pos), file=stderr)
        print(f"<{file}> " + repr(error), file=stderr)
        return


def run(file):
    stdout = open(f"{d}\\snow.stdout", "w")
    stderr = open(f"{d}\\snow.stderr", "w")

    run_f(file, stdout, stderr)

    stdout.close()
    stderr.close()


if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2:
        run(sys.argv[1])

    print("ran")
    os.system("pause")
