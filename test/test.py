from core.lexer.lexer import Lexer


with open("test.snow", "r") as f:
    code = f.read()

lexer = Lexer(code)
tokens = lexer.lex()
print(tokens)
