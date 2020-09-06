import Interpreter
import Lexer
import Parser


def run(filename):
    with open(filename, "r") as f:
        data = "\n".join(f.readlines())

        lexer = Lexer.Lexer(data)
        a = list(lexer.lex())

        parser = Parser.Parser(a)
        b = parser.parse()

        inter = Interpreter.Interpreter()
        c = inter.run(b)

        return c


if __name__ == "__main__":
    run("test.snow")
