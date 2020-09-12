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


def lint(filename):
    with open(filename, "r") as f:
        data = "\n".join(f.readlines())

        lexer = Lexer.Lexer(data)
        a = list(lexer.lex())

        parser = Parser.Parser(a)
        b = parser.parse()

        b = [repr(bb) for bb in b]
        for i, x in enumerate(b[1:]):
            if b[i][-1] not in (")", "}", "\""):
                b[i+1] = " " + x

        return "".join(b)


if __name__ == "__main__":
    run("test.snow")
    print(lint("test.snow"))
