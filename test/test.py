from core.lexer.lexer import Lexer

with open("test.snow", "r") as f:
    code = f.read()

lexer = Lexer(code)
res = lexer.lex()
tokens, error = res

if error:
    print(error)

else:
    print("\n".join(map(repr, tokens)))
